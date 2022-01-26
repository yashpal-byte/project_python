x = [2,3,4,5,6]
i = 0
j = 0
mul = 1
while i<len(x):
    i = i + 1
    mul = mul * x[i]*x[i+1]
    j = j + 2
    
print(mul)