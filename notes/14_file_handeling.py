# notes on file handeling in python

# check if file exists using os and pathlib modules
import os
from pathlib import Path

# using os module
print("Current working directory:", os.getcwd())
print("List of files in current directory:", os.listdir())

if os.path.exists('notes/practice.txt'):
    print('File exists')
else:    
    print('File does not exist')

# using pathlib module
file_path = Path('notes/practice.txt')
if file_path.exists():
    print('File exists')
else:    
    print('File does not exist')

# creating a file and writing to it using append mode
with open('notes/practice.txt', 'a+') as file:
    file.write('This is a practice file for file handling in Python.\n')
    file.write('We are learning how to read and write files.\n')
    file.write('This file will be used for demonstration purposes.\n')

# reading from a file
    file.seek(0)  # move file pointer to beginning of file
    print('File content:\n using read()', file.read())

# reading from a file using readline()
    file.seek(0)  # move file pointer to beginning of file
    print(f"readline Line: {file.readline()}")

# reading from a file using readlines()
    print('File content:\n using readlines()')
    lines = file.readlines()
    for line in lines:
        print(f"readlines Line: {line.strip()}")

