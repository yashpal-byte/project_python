#Python program to sum of the first n positive integers

def sum_of_n(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s
n = 5
print(sum_of_n(n))