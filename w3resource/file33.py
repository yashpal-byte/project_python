#Python program to sum of three given integers. However, if two values are equal sum will be zero.
x = int(input("x "))
y = int(input("y "))
z = int(input("z "))
sum = x+y+z
if x == y or x==z or y==z:
    print(0)
else:
    print(sum)


