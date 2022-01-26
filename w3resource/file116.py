#Python program to print Unicode characters
x = int(input('enter number '))
lst = []
if x > 0:
    while x>0:
        x = x - 1
        cube = x**3
        #x = x - 1
        lst.append(cube)
print(lst)
add = 0
for i in lst:
    add = add + i
print(add)