import PIL
from PIL import Image
import os
from os import listdir
from os.path import isfile, join

def createMultipleVersionsOfFile(filename):
    percents = [1, 0.82, 0.57, 0.42, 0.27, 0.2]
    directories = ['drawable-xxxhdpi', 'drawable-xxhdpi',
                   'drawable-xhdpi', 'drawable-hdpi',
                   'drawable-mdpi', 'drawable-ldpi']

    for index, i in enumerate(percents):
        img = Image.open(filename)
        basewidth = int(img.size[0]*i)
        print(basewidth)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
        print(directories[index])
        img.save(directories[index]+'/'+filename)

onlyfiles = [f for f in listdir(os.path.dirname(os.path.abspath(__file__))) if isfile(join(os.path.dirname(os.path.abspath(__file__)), f))]

for i in onlyfiles:
    if '.py' not in i:
        print(i)
        createMultipleVersionsOfFile(i)
