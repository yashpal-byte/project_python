#41. Write a Python program to check whether a file exists.

import os.path
print(os.path.isfile('file41.txt'))
print(os.path.isfile('file41.py'))

print(os.getcwd())