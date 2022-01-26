#Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum

a = int(input('a '))
b = int(input('b '))
c = int(input('c '))

if a == b == c:
    print((a+b+c)*3)
else:
    print(a+b+c)
