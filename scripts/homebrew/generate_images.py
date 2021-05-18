import os
from os import listdir
from os.path import isfile, join
import random
from shutil import copyfile, copytree

IMAGE_FOLDER_PATH = "./Tensorflow/data/images"
LABEL_IMG_FOLDER = "./Tensorflow/workspace/training_demo/images"
filelist = None

def listFile(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def placeFile(name):
    print(f"copying {name}...")
    os.symlink(os.path.abspath(f"{IMAGE_FOLDER_PATH}/{name}"), os.path.abspath(f"{LABEL_IMG_FOLDER}/{name}"))

def main():
    global filelist

    print("run main...")
    filelist = list(listFile(IMAGE_FOLDER_PATH))

    for name in filelist:
        placeFile(name)

if __name__ == "__main__":
    main()