from pathlib import Path
import shutil
from datetime import datetime
import time
from rich import print

from get_oldest_directory import get_oldest_dir


class DirManager():
    def __init__(self, src: str):
        self.src = Path(src)

    def relocation(self, suffixes: list | str, dst: str) -> None:
        if not self.src.is_dir():
            print('Источник либо не является директорией, либо не существует.')
            return

        dst = Path(dst)

        for file in self.src.iterdir():
            if not dst.exists():
                dst.mkdir()

            if Path(file).suffix in suffixes:
                try:
                    shutil.move(file, dst)
                    print(f'"{file.name}" успешно перемещен.')

                except (OSError) as e:
                    print(
                        f'При перемещении: {file} возникла ошибка:\n\t{e}')

    def delete(self, suffixes: list | str) -> None:
        for file in self.src.iterdir():
            if Path(file).suffix in suffixes:
                try:
                    Path(file).unlink()
                    print(f'{file} успешно удален.')

                except (FileNotFoundError, OSError) as e:
                    print(
                        f'При удалении файла: {file} возникла ошибка:\n\t{e}')


def backup(src: str, dst: str, interval=5, count=5) -> None:
    src, dst = Path(src), Path(dst)

    if not dst.exists():
        dst.mkdir()

    if not len(list(dst.iterdir())) < count:
        shutil.rmtree(get_oldest_dir(dst))

    backup_time = datetime.today().strftime('%Hh%Mm%Ss')
    new_file_name = (f'backup__{src.name}__{backup_time}')

    try:
        shutil.copytree(src, dst.joinpath(new_file_name))

    except (OSError) as e:
        print(f'При создании резервной копии возникла ошибка:\n\t{e}')

    time.sleep(interval)
