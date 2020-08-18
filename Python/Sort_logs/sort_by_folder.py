# -*- coding: utf-8 -*-
#python.exe sort_by_folder.py --dir d:fototemp --out d:fotores --time %Y-%m/%Y-%m-%d
from email.policy import default

import os
import argparse
import glob
import time
import shutil

cmd = argparse.ArgumentParser(description="Копирует файлы по папкам с датой создания")
cmd.add_argument("--dir", "-d", type=str, default="", help="Каталог с файлами")
cmd.add_argument("--ext", "-e", type=str, default="*.jpg", help="Расширение файлов")
cmd.add_argument("--out", "-o", type=str, default="", help="Каталог с результатом")
cmd.add_argument("--time", "-t", type=str, default="%Y-%m-%d", help="Шаблон папки результата")
cmd.add_argument("--move", "-m", type=int, default=1, help="Перемещать файлы (иначе копировать)")

args = cmd.parse_args()

dir_work = os.path.realpath(args.dir)
dir_out = os.path.realpath(args.out)

if not os.path.exists(dir_work):
    print("dir not exist: " + dir_work)
    exit()

if not os.path.exists(dir_out):
    print("dir not exist: " + dir_out)
    exit()

maska = os.path.join(dir_work, args.ext)
listFile = glob.glob(maska)
print(maska)
for nameFile in listFile:
    onlyName = os.path.basename(nameFile)
    timeStr = time.strftime(args.time, time.gmtime(os.path.getmtime(nameFile)))

    # Новый каталог и полный путь
    newDir = os.path.join(dir_out, timeStr)
    newFullPath = os.path.realpath(os.path.join(newDir, onlyName))
    print(onlyName + " => " + newFullPath)

    if not os.path.exists(newDir):
        os.makedirs(newDir)

    if args.move == 1:
        shutil.move(nameFile, newFullPath)
    else:
        shutil.copy(nameFile, newFullPath)