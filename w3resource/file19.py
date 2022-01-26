#Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
b = input('string ')

if "Is" in b[0:2]:
    print(b)
else:
    c = "Is" + b[0:]
    print(c)