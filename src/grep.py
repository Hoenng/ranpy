#grep.py

import sys
from pathlib import Path

def fileRead(searchString, filepath):
    
    with open(filepath) as myFile:
        for num, line in enumerate(myFile, 1):
            if searchString in line:
                print ("Line: {} {}".format(num, line))

def main():

    searchString=sys.argv[1] 
    searchPath=sys.argv[2]

    filepath =  Path(searchPath)
    
    print("We are looking for {} in {}".format(searchString, filepath))
    
    fileRead(searchString, filepath)

if __name__ == '__main__':
    main()