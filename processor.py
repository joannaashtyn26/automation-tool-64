import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    pass


class DataProcessor:
    def __init__(self, required_fields: Dict[str, type]):
        self.required_fields = required_fields

    def validate(self, data: Any) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise ValidationError("input data must be a dictionary")
        
        validated = {}
        for field, expected_type in self.required_fields.items():
            if field not in data:
                raise ValidationError(f"missing required field: {field}")
            
            val = data[field]
            if not isinstance(val, expected_type):
                try:
                    val = expected_type(val)
                except (ValueError, TypeError) as exc:
                    raise ValidationError(
                        f"field '{field}' could not be converted to {expected_type.__name__}"
                    ) from exc
            validated[field] = val
        return validated

    def process_batch(self, batch: List[Any]) -> Tuple[List[Dict[str, Any]], List[str]]:
        processed_items = []
        errors = []
        for index, item in enumerate(batch):
            try:
                valid_data = self.validate(item)
                valid_data["status"] = "verified"
                processed_items.append(valid_data)
            except ValidationError as err:
                error_msg = f"item {index} validation error: {err}"
                logger.warning(error_msg)
                errors.append(error_msg)
        return processed_items, errors