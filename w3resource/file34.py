#Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
x = int(input('x '))
y = int(input('y '))
sum = x + y
if sum in range(15,21):
    print(20)
else:
    print(sum)