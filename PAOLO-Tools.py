import os
import sys
import argparse
import shutil
from PIL import Image
import json
from natsort import os_sorted

# json manipulation
def saveJSON(data, filePath):
    with open(filePath, 'w') as f:
        json.dump(data, f, indent = 2)

def loadJSON(filePath):
    with open(filePath, 'r') as file:
        return json.load(file)

# sets up arguments to be accessible
parser = argparse.ArgumentParser(prog='PAOLO-Tool', description='it should make volume')
parser.add_argument('inputFolder', metavar='INPUT_FOLDER', type=str, help='source images folder')
parser.add_argument('volumeNumber', metavar='VOLUME_NUMBER', type=str, help='volume number, to create folder')
args = parser.parse_args()

# sets up variables and stuff
inputFolder = args.inputFolder
volumeNumber = args.volumeNumber
INDEX = 0
FOLDER_INDEX = 0

if inputFolder[-1] != '\\' and inputFolder[-1] != '/': inputFolder += '/'
if volumeNumber[-1] != '\\' and volumeNumber[-1] != '/': volumeNumber += '/'

# this section does stuff with images
def saveImage(image, folder):
    global INDEX
    INDEX += 1
    image.save(folder + str(INDEX) + '.webp', 'webp', quality = 80, method = 6)
    # image.save(folder + str(INDEX) + '.jpg', 'jpeg', quality = 80, optimize = True, progressive = True)

def resizeImage(f, image):
    width, height = image.size
    if height > 1600:
        newWidth = int(width * 1600 / height)
        newHeight = 1600
        image = image.resize((newWidth, newHeight))
        print(f, 'is too big. Resizing to', newWidth, 'x', newHeight)
    return image

def cutInHalfImage(image):
    width, height = image.size
    leftImage = image.crop((0, 0, width / 2, height))
    rightImage = image.crop((width / 2, 0, width, height))
    return (leftImage, rightImage)
    
# here's function that uses those funcions with images
def convertImages(input, output):
    for f in os_sorted(os.listdir(input)):

        fName, fExt = os.path.splitext(f)
        image = Image.open(input + f)
        width, height = image.size
        
        if width > height:
            print(f + ' is double page')
            left, right = cutInHalfImage(image)
            saveImage(resizeImage(f, left), output)
            saveImage(resizeImage(f, right), output)
        else:
            print(f + ' is a normal page')
            saveImage(resizeImage(f, image), output)

def createFolder():
    global FOLDER_INDEX
    chapterFolder = volumeNumber + str(FOLDER_INDEX+1)
    os.mkdir(chapterFolder)
    FOLDER_INDEX += 1
    print('made corresponding ' + chapterFolder)
    
def main():
    # configuring json
    volumeJSON = volumeNumber + 'config.json'

    global FOLDER_INDEX
    global INDEX
    # if volume folder don't exist then generate it
    if not os.path.isdir(volumeNumber): os.mkdir(volumeNumber)
    
    # loop for counting the images and chapters in the base folder and then creating folders and converting images to them
    for f in os_sorted(os.listdir(inputFolder)):
        print("\ninput folder name: " + f)
        createFolder()
        print("")

        convertImages(inputFolder + f + '/', volumeNumber + str(FOLDER_INDEX) + '/')
        
        # json creating/updating
        volumeConfig = {}
        if os.path.isfile(volumeJSON):
            volumeConfig = loadJSON(volumeJSON)
            volumeConfig['numPages'] += [INDEX]
            print("\nupdating json")
        else:
            volumeConfig['numPages'] = [INDEX]
            print("\njson doesn't exist, creating it")
        saveJSON(volumeConfig, volumeJSON)
        
        INDEX = 0

main()