
import sys
from pathlib import Path

class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 
        
    def check(self, key):
        wordcount = self.get(key, 0)
        return(wordcount)
    
def countWords(filepath, caseFlag, worddict):

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            if caseFlag:
                line = line.lower()
            linewords = line.split()
            for word in linewords:
                wordcount = worddict.check(word)
                wordcount = wordcount+1
                worddict.add(word, wordcount)
    return worddict
 
def writeWords(worddict):
    file_out = open('dict_list.csv', 'w')
    for key, value in worddict.items():
        dictstr = (key + ' , ' + str(value)+ '\n')
        file_out.write(dictstr)
    file_out.close()
         
# Main Function 

def main():
    
    searchPath=sys.argv[1]
    caseInSensitive=sys.argv[2]
    filepath =  Path(searchPath)
    
    worddict = my_dictionary()
    
    if (caseInSensitive == 'Y'):
        caseFlag = True
    else:
        caseFlag = False
    
    wordsCounted = countWords(filepath, caseFlag, worddict)
    
    writeWords(wordsCounted)

    
   
    
if __name__ == '__main__':
    main()