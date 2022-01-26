lst = [20, 30, 40, 50, 60, 70, 80]

for i in lst:
    print(i > 30)
print()   
print(all(x>1 for x in lst))
print(any(x>40 for x in lst))