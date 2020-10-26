import os
import logging

matches = 0
def find(filename,path):
    global matches
    files = os.listdir(path)
    d = {}
    d['folders'] = []
    for file in files:
        try:
            if(os.path.isfile(path+'\\'+file)):
                if(filename.lower() in file.lower()):
                    print('File Found:',path+'\\'+file)
                    matches+=1
                    continue
            else:
                d['folders'].append(file)
        except:
            logging.warning('Access Denied for path : ' + path)
    for ep in d['folders']:
        try:
            find(filename, path+'\\'+ep)
        except:
            logging.warning('Access Denied for path : ' + path)
	

filename = input("Enter Full or Partial File Name: ")
path = input("Enter Directory to search in: ")
find(filename,path)
print('Search Complete.',matches,'matches found')

