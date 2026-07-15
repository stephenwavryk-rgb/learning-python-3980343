#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path
    
# Open the file and read the contents
# sample_file = open("textfile.txt","r")

# Path 1 and filename
# path = "c:\Users\Stephen\OneDrive\CondoBoard"
filename = "YCC318_Owners2.txt"
# Join various path components
# Construct the full path
full_path = os.path.join("C:","Users", "Stephen", filename)
print(os.path.join(full_path))

# print("Item exists:", path.exists(full_path))
# print("Here is the list of folders in", os.listdir())

# Reading and writing files using the full path
# with open(full_path, "r") as file:
#     content = file.read()
#     print(content)

# Current working directory
# current_dir = os.getcwd()

# List files in the current directory
# files_in_dir = os.listdir(path)

# # Iterate over files and print their full paths
# for file_name in files_in_dir:
#     file_path = os.path.join(path, file_name)
#     print(file_path)

sample_file = open(full_path,"r")
if sample_file.mode == 'r':
    # use the read() function to read the entire file
    #contents = sample_file.read()
    #print(contents)
    file_lines = sample_file.readlines()
    for line in file_lines:
        print(line)

# ---------------------

# my_file = open("newfile.txt", "r")