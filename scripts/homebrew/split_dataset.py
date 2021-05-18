import os
from os import listdir, remove
from os.path import isfile, join, split, splitext
import random
import sys

IMAGE_FOLDER_PATH = "./Tensorflow/workspace/training_demo/images"
SAMPLE_RATE = 0.1
filelist = None

if(len(sys.argv) == 1):
    SAMPLE_RATE = float(sys.argv)

testImage = []

def listFile(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def file_filter():
    global filelist

    removeItem = []

    for item in filelist:
        _, ext = splitext(item)
        if(ext == ".xml"):
            removeItem.append(item)
    
    for item in removeItem:
        filelist.remove(item)
    
    print(filelist)

def pickup():
    global filelist, testImage

    index = random.randint(0,len(filelist)-1)
    item = filelist[index]
    del filelist[index]

    testImage.append(item)

def placeFile(name, folder):
    print(f"copying {name}...")
    filename, ext = splitext(name)
    os.symlink(os.path.abspath(f"{IMAGE_FOLDER_PATH}/{filename}{ext}"), os.path.abspath(f"{IMAGE_FOLDER_PATH}/{folder}/{name}{ext}"))
    os.symlink(os.path.abspath(f"{IMAGE_FOLDER_PATH}/{filename}.xml"), os.path.abspath(f"{IMAGE_FOLDER_PATH}/{folder}/{name}.xml"))

def main():
    global filelist, testImage

    print("run main...")
    filelist = list(listFile(IMAGE_FOLDER_PATH))
    file_filter()

    totalSize = len(filelist)
    for i in range(int(totalSize*SAMPLE_RATE)):
        pickup()
    
    # print(filelist)
    
    for name in filelist:
        placeFile(name,"train")
    for name in testImage:
        placeFile(name,"test")

if __name__ == "__main__":
    main()