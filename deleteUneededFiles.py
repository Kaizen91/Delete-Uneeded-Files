#! /Users/stephenlang/anaconda/bin/python
#deleteUneededFiles.py - Walks through a folder tree and prints the names of files that
#are over 100MB

#Calling os.path.getsize(path) will return the size in bytes of the file in the
#  path argument.
import os

path = os.path.abspath('../../../..')
for folderName, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if os.path.getsize(os.path.join(folderName, filename)) > 100:
            sizeMB = os.path.getsize(os.path.join(folderName, filename)) / 1000000
            print(filename + ' : ' + str(sizeMB))
        else:
            continue
      
