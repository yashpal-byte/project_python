# Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
num = int(input('num '))
b = 17

if b>num:
    print(b-num)
else:
    print((num-b)*2)