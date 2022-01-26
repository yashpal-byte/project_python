#Python program to count the number 4 in a given list
n = int(input())
b = []
for i in range(1,n+1):
    c = int(input('enter '))
    b.append(c)
print(b)

i = 0
j = 0
k = 0
while i<len(b):
    if b[k] == 4:
        j = j + 1
    k = k + 1
    i = i + 1
print(j)