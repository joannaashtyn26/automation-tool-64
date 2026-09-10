import os
import shutil
from pathlib import Path
from typing import Union

def clean_directory(path: Union[str, Path], pattern: str = '*') -> None:
    target = Path(path)
    if not target.is_dir():
        raise ValueError(f'directory not found: {path}')
    for item in target.glob(pattern):
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

def organize_files(source: str, destination: str, extension: str) -> None:
    src_path = Path(source)
    dst_path = Path(destination)
    dst_path.mkdir(parents=True, exist_ok=True)
    for file in src_path.glob(f'*.{extension}'):
        shutil.move(str(file), str(dst_path / file.name))

def get_directory_size(path: str) -> int:
    return sum(f.stat().st_size for f in Path(path).rglob('*') if f.is_file())

def validate_paths(paths: list[str]) -> bool:
    return all(Path(p).exists() for p in paths)

def format_byte_size(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f'{size:.2f} {unit}'
        size /= 1024
    return f'{size:.2f} TB'