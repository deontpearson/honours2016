import os, sys, hashlib

STORED_FILES = {}
dir = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]

def getStoredFiles():
    "Reads the exisiting stored filenames and hashes from a file"
    if os.path.isfile(dir + '/data/filenames.dat'):
        with open(dir + '/data/filenames.dat', 'r') as f:
            for line in f:
                temp = line.replace('\n', '').split(':')
                if not len(temp) == 1: # accounts for an empty file
                    STORED_FILES[temp[0]] = temp[1].split(',')

def saveStoredFiles():
    "saves the filenames from dictionary to stats.info"
    tempString = ""
    with open(dir + '/data/filenames.dat', 'w+') as f:
        for l in STORED_FILES:
            tempString += l + ":" # adds the hash value to the string
            for item in STORED_FILES[l]:
                tempString += item + ',' # adds the list item to the string
            tempString = tempString[:-1] # removes the last , from the string
            tempString += "\n" # puts each string on a new line
        f.write(tempString)

def saveFileToDisk(filename, fileContents):
    "This function processes the POST request and saves the uploaded file to the server"
    if STORED_FILES == {}:
        getStoredFiles() # gets all the files stored on the server
    hashValue = hashlib.sha1(fileContents).hexdigest() # hash the file
    if hashValue in STORED_FILES:
        if filename not in STORED_FILES[hashValue]: # checks if the filename is already in the dictionary with the same hash if it is not it adds it
            STORED_FILES[hashValue].append(filename)
    else:
        if not os.path.exists(dir + '/data/uploads'):
            os.makedirs(dir + '/data/uploads')
        STORED_FILES[hashValue] = [filename] # save the filename to STORED_FILES
        open(os.path.join(dir + '/data/uploads/', hashValue), "w").write(fileContents) # save the file to disk
    saveStoredFiles()
