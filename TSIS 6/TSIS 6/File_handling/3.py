#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.

import os

path = r"C:\\Users\\Daniyar\\Documents\\GitHub\\pp2\\TSIS 6\\TSIS 6\\File_handling"

print(os.path.exists(path))
print(os.path.basename(path))
print(os.path.dirname(path))