#Python program to test whether a number is within 100 of 1000 or 2000
b = int(input('num '))

if b in range(900,1101) or b in range(1900,2101):
    print("it is within 100 of 1000 or 2000")
else:
    print("it is not within 100 of 1000 or 2000")
    