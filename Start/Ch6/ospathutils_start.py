#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path

import time
from datetime import datetime

# Print the name of the OS
# print(os.name)

# # Check for item existence and type
# print("Item exists:", path.exists("textfile.txt"))
# print("Item is a file:", path.isfile("textfile.txt"))
# print("Item is a directory:", path.isdir("textfile.txt"))

# # Work with file paths
# print("Item's path:", path.realpath("textfile.txt"))
# print("Item's path and name:", path.split(path.realpath("textfile.txt"))) # split function so to see it separately

# # Get the modification time
# t = time.ctime(path.getmtime("textfile.txt"))
# print(t)
# print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

# # Calculate how long ago the item was modified
# td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
# print(f"It has been {td} since the file was modified") # interpretive f string
# print(f"Or, {td.total_seconds()} seconds")

# print(path.exists("deps"))
# print(path.isdir("deps"))
# os.path.getsize(path, /)
# os.chdir(path)
# print("Here is the list of folders in", os.listdir())
cwd = os.getcwd()
print(cwd)
# print("Here is the list of folders in", os.listdir())
# os.chdir("/workspaces")
# print("Working dir is ", os.getcwd())
# print("Here is the list of folders in", os.listdir())
# os.chdir("/")
# print("Working dir is ", os.getcwd())
# print("Here is the list of folders in", os.listdir())
# os.chdir("/workspaces/.codespaces")
# print("Working dir is ", os.getcwd())
# print("Here is the list of folders in", os.listdir())

# os.chdir("/usr")
# print("Working dir is ", os.getcwd())