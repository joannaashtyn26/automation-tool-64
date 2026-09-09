import concurrent.futures
from typing import Callable, Iterable, List, TypeVar, Generator

T = TypeVar('T')

R = TypeVar('R')


class BatchProcessor:
    def __init__(self, max_workers: int = 4, chunk_size: int = 100):
        self.max_workers = max_workers
        self.chunk_size = chunk_size

    def _chunk_iterable(self, iterable: Iterable[T]) -> Generator[List[T], None, None]:
        chunk = []
        for item in iterable:
            chunk.append(item)
            if len(chunk) == self.chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

    def process(self, func: Callable[[T], R], items: Iterable[T]) -> List[R]:
        results = []
        chunks = list(self._chunk_iterable(items))
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self._process_chunk, func, chunk)
                for chunk in chunks
            ]
            for future in concurrent.futures.as_completed(futures):
                results.extend(future.result())
        return results

    @staticmethod
    def _process_chunk(func: Callable[[T], R], chunk: List[T]) -> List[R]:
        return [func(item) for item in chunk]
