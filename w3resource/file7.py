#7. Write a Python program to accept a filename from the user and print the extension of that.
file = input('file ')
filename = file.split('.')
print(filename[-1])
