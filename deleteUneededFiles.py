#! /Users/stephenlang/anaconda/bin/python
#deleteUneededFiles.py - Walks through a folder tree and prints the names of files that
#are over 100MB

import os

path = os.path.abspath('../../../../..')
print(path)
for folderName, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if os.path.getsize(os.path.join(folderName, filename)) > (100*1000000):
            sizeMB = os.path.getsize(os.path.join(folderName, filename)) / 1000000
            print(folderName + filename + ' : ' + str(sizeMB))
        else:
            continue
      
