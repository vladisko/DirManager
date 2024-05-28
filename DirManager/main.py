import os
from shutil import copytree, rmtree
import threading

from datetime import datetime
from get_oldest_directory import get_oldest_dir


class DirManager:
    class Extensions:
        def __init__(self, src, extensions):
            self.src = src
            self.extensions = extensions

        def relocation(self, dst: str):
            if not os.path.exists(self.src):
                print(f'Директория источник "{self.src}" не существует')
                return

            if not os.path.exists(dst):
                os.mkdir(dst)

            dir_files = os.listdir(path=self.src)

            for file in dir_files:
                ext = file.split('.')[-1]

                if ext in self.extensions:
                    try:
                        os.replace(f'{self.src}\\{file}', f'{dst}\\{file}')
                    except (OSError, FileNotFoundError) as e:
                        print(f'Ошибка перемещения {file} : {e}')

        def delete(self):
            if not os.path.exists(self.src):
                print(f'Директория источник "{self.src}" не существует')
                return

            dir_files = os.listdir(path=self.src)

            for file in dir_files:
                ext = file.split('.')[-1]

                if ext in self.extensions:
                    try:
                        os.remove(f'{self.src}\\{file}')
                    except (OSError, FileNotFoundError) as e:
                        print(f'{file} : {e}')

    def backup(self,
               src: str,
               dst: str,
               create_interval: int,
               delete_interval: int,
               max_backup_num: int,
               ) -> None:

        self.src = src
        self.dst = dst
        self.max_backup_num = max_backup_num

        if not os.path.exists(src):
            print(f'Директория источник "{src}" не существует')
            return

        if not os.path.exists(dst):
            os.mkdir(dst)

        create_th = threading.Timer(create_interval, self.__create)
        create_th.start()

        delete_th = threading.Timer(delete_interval, self.__delete)
        delete_th.start()

    def __create(self) -> None:
        world_name = self.src.split('\\')[-1]
        backup_time = datetime.today().strftime('%H-%M-%S')
        backup_name = f'backup__{world_name}__{backup_time}'

        copytree(self.src, os.path.join(self.dst, backup_name))

    def __delete(self) -> None:
        if not len(os.listdir(path=self.dst)) <= self.max_backup_num:
            oldest_dir = get_oldest_dir(self.dst)

            if oldest_dir:
                rmtree(oldest_dir)
