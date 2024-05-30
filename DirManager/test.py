from main import *
import time
DIR = 'S:\Downloads'
DST = 'S:\Images'

SRC = 'S:\ProgrammingProjects\Python\DirManager\\backup_obj'
BACKUPS_DIR = 'S:\ProgrammingProjects\Python\DirManager\\backups'

# while True:
#    backup(SRC, BACKUPS_DIR, 3600)

DirManager(DIR).relocation(['.png', '.jpg', '.jpeg'], DST)

# DirManager(DIR).delete('.exe')

input()
