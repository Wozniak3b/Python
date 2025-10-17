#!/usr/bin/env python3
import os
from typing import Generator, Iterable

COUNT_DIRECTORY = r"C:\Prywatne\Inne\Muza\Quark"
RECURSIVE_DIRECTORY = r"C:\Prywatne\Inne\Filmy"

def count_files(path: str) -> int:
    with os.scandir(path) as it:
        return sum(1 for entry in it if entry.is_file())

def dir_tree(path: str) -> Generator[str, None, None]:
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    yield entry.path
                elif entry.is_dir():
                    yield from dir_tree(entry.path)
    except PermissionError:
        return

if __name__ == "__main__":
    try:
        n = count_files(COUNT_DIRECTORY)
        print(f"Number of files in: {COUNT_DIRECTORY}: {n}")
    except FileNotFoundError:
        print(f"Directory doesn't exist: {COUNT_DIRECTORY}")
    except NotADirectoryError:
        print(f"Not a directory: {COUNT_DIRECTORY}")

    print(f"Tree of directories: {RECURSIVE_DIRECTORY}:")
    for path in dir_tree(RECURSIVE_DIRECTORY):
        print(path)
