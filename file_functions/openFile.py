import sqlite3
import os

def open_file(readingFile):
    with open(readingFile, 'r') as pipeFile:
        fileLines = pipeFile.readlines()
    return fileLines