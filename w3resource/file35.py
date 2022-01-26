#Python program that will return true if the two given integer values are equal or their sum or difference is 5.
x = int(input('x '))
y = int(input('y '))
sum = x + y
if sum == 5:
    print(True)
elif x==y:
    #sum == True
    print(True)
elif abs(x-y)==5:
    print(True)
else:
    print(sum) 