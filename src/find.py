#find.py

import sys
import os
import enum
from pathlib import Path


#Example ./find.py '/mnt/d/bin/' -name '*.py'. 
#Example ./find.py '/mnt/d/bin/' -size 1MB. 
#Example .\find.py D:\bin\ -name '*.py'.
#Example .\find.py D:\bin\ -size 1MB. 
#That trailing / is essential

 
def findFile(search_dir,search_type, search_object):

    # if it is a size search search_object will contain size
    # move that value to search_size and change search_object
    # to wildcard * so it will look for all files
    
    if search_type == '-size':
        search_size = search_object
        search_object = '*'
        reqSize = search_size[0:-2]
        sizeUnitCode = search_size[-2:]
        if sizeUnitCode == 'KB':
            reqSizeB = int(reqSize) * 1024
        elif sizeUnitCode == 'MB':
            reqSizeB = int(reqSize) * 1024 * 1024
        elif sizeUnitCode == 'GB':
            reqSizeB = int(reqSize) * 1024 * 1024 * 1024
    #print("Required size of "  + reqSize + sizeUnitCode + "in bytes is " + str(reqSizeB))    

    print("Now looking for " + str(search_dir))

    for file in Path(search_dir).rglob(search_object):
        #if size is wanted tag in a call to file_size
        # check size against requirement
        # print if it meets
        if search_type == '-size':
            fileSize = file_size(file)
            #print("File size and required size are " + str(fileSize) + "and" + reqSizeB)
            if int(fileSize) >= int(reqSizeB):
                print(str(file) + ' ' + str(fileSize) + ' ' +  str(reqSizeB) + ' ' + sizeUnitCode) 
        if search_type == '-name':
        #otherwise if name search print names
            print(file)
    return



def file_size(fname):
    statinfo = os.stat(fname)
    return statinfo.st_size

def main():

    search_dir=sys.argv[1] # can be . or full or relative path (but not yet ..). Will search recursively downwards
    search_type=sys.argv[2] # -name, -size 
    search_object=sys.argv[3] #filename or file minimum size
    print('We are here!')
    

    # if . has been passed as the dir it needs to be changed to full path
    if search_dir == '.':
        search_dir = Path.cwd()

    print('Target directory, search type and search object is ' + str(search_dir) + search_type + search_object)

    findFile(search_dir,search_type, search_object)

if __name__ == '__main__':
    main()
    