#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

data = input().split(',')
lst = []
for i in data:
    x = int(i)
    lst.append(x)
tup = tuple(lst)
print(lst, end=': ')
print(tup)
