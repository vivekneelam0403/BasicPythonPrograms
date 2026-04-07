import json
import os

def log():
    pass

def getBufferSizeInLines():
    pass

def getMaxSpace():
    pass

logMessage = log()
fileSize = os.path.getsize('logFile_1.txt')
fileCounter = 1
maxSpace = getMaxSpace()
buffer = ""
counter = 0

def getFileName():
    global fileSize 
    global fileCounter
    global maxSpace

    while fileSize > maxSpace:
        if fileSize <= maxSpace:
            currentFileName = f"log_{fileCounter}.txt"
            renamedFile = f"log_{fileCounter + 1}.txt"
            os.rename(currentFileName, renamedFile)
            fileCounter += 1
            return os.rename
        else:
            currentFileName = f"log_{fileCounter}.txt"
            renamedFile = f"log_{fileCounter + 1}.txt"
            os.rename(currentFileName, renamedFile)
            fileCounter += 1
        

def flushLogs():
    global buffer 
    global counter
    fileName = getFileName()

    if buffer != "":
        with open(fileName, "a") as file: 
            file.write(buffer)
            counter = 0
            buffer = ""
    else:
        with open(fileName, "a") as file: 
            file.write(buffer)
            counter = 0
            buffer = ""

def logToFile(logMessage):
    global buffer
    global counter
    bufferSize = getBufferSizeInLines()
    
    if counter < bufferSize:
        buffer = buffer + logMessage + "\n"
        counter += 1
    else:
        flushLogs()