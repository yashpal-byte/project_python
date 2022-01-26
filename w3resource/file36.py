#Python program to add two objects if both objects are an integer type
def num(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x+y
    else:
        print('not integers')
    #return x + y
x = '5'
y = 6.3
print(num(x,y))