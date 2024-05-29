from os.path import getctime
from pathlib import Path


def get_oldest_dir(directory: str) -> str | None:

    directories = []
    for file in directory.iterdir():

        path = Path(directory).joinpath(file)
        if Path(path).is_dir():
            directories.append(path)

    if not directories:
        return None

    oldest_dir = min(directories, key=getctime)
    return oldest_dir
