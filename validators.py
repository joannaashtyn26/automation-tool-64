from functools import lru_cache
import re

class DataValidator:
    def __init__(self, pattern: str = r"^[a-zA-Z0-9_]+$"):
        self._pattern = re.compile(pattern)

    @lru_cache(maxsize=128)
    def validate_id(self, identifier: str) -> bool:
        return bool(self._pattern.match(identifier))

    @staticmethod
    def batch_validate(items: list[str], chunk_size: int = 1000) -> list[bool]:
        results = []
        for i in range(0, len(items), chunk_size):
            chunk = items[i:i + chunk_size]
            results.extend([bool(re.match(r"^\d+$", item)) for item in chunk])
        return results

    def process_payload(self, data: dict) -> dict:
        return {k: v for k, v in data.items() if v is not None}

    def fast_filter(self, stream: list[str], limit: int) -> list[str]:
        return list(filter(None, stream))[:limit]