#Python program to filter the positive numbers from a list.
x = [-1, 2, -3, 4, -5,6,-7,8,-9,10]
lst = list(filter(lambda a : a>0, x))
print(lst)