import os
import sys
import argparse
import shutil
from PIL import Image
import json
from natsort import os_sorted


parser = argparse.ArgumentParser(prog='Okuma-Tools', description='A collection of tools to manage your Okuma-Library.')
parser.add_argument('libraryFolder', metavar='LIBRARY_FOLDER', type=str, help='the library folder. If it doesn\'t exist, creates it.')
parser.add_argument('slug', metavar='SLUG', type=str, help='the name of the folder used in the LIBRARY_FOLDER. I.e. my-book-title')

parser.add_argument('title', metavar='TITLE', type=str, help='title of your manga')
parser.add_argument('booktype', metavar='BOOKTYPE', type=str, help="sets book type")
parser.add_argument('vols', metavar='VOLUMES', type=int, help="sets volume number")
parser.add_argument('ext', metavar='EXTENSION', type=str, help="sets image extension")
parser.add_argument('--jp', help="sets japanese order", action="store_true")




args = parser.parse_args()
title = args.title
booktype = args.booktype
vols = args.vols
ext = args.ext
jp = args.jp



libraryFolder = args.libraryFolder
if libraryFolder[-1] != '\\' and libraryFolder[-1] != '/': libraryFolder += '/'


bookSlug = args.slug



def saveJSON(data, filePath):
    with open(filePath, 'w') as f:
        json.dump(data, f, indent = 2)

def loadJSON(filePath):
    with open(filePath, 'r') as file:
        return json.load(file)
        
        
        
        
        
def main():

    titleFolder = libraryFolder + bookSlug + '/'

    libraryJSON = libraryFolder + 'config.json' 
    titleJSON = titleFolder + 'config.json'


    # Create the folders
    if not os.path.isdir(libraryFolder): os.mkdir(libraryFolder)
    os.mkdir(titleFolder)


    # Create the files
    if os.path.isfile(libraryJSON):
        libraryConfig = loadJSON(libraryJSON)
        if bookSlug not in libraryConfig["titles"]:
            libraryConfig["titles"] += [bookSlug]
    else:
        libraryConfig = {}
        libraryConfig["titles"] = [bookSlug]
    saveJSON(libraryConfig, libraryJSON)

    titleConfig = {}
    titleConfig['title']            = title
    titleConfig['bookType']         = booktype
    titleConfig['numVolumes']       = vols
    titleConfig['fileExtension']    = ext
    titleConfig['japaneseOrder']    = jp
    saveJSON(titleConfig, titleJSON)
    
main()