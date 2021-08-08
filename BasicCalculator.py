#create a calculator which does arithmetic operations with 2 numbers
print('Input your choice of operations')
print('a for addition')
print('s for subtraction')
print('m for multiplication')
print('d for division')

input('Choice: ')
x = int(input('Enter First number: '))
y = int(input('Enter second number: '))

def arithmetic(x, y):
    
    if a:
        add = x + y #addition
        print(add)
    elif s:
        if x>y:
            sub = x-y
            print(sub)
        else:
            sub = y-x
            print(sub)
    elif m:
        multiplication = x*y #multiplication
        print(multiplication)
    elif d:
        if x>y:
            div = x/y
            print(div)
        else:
            div = y/x
            print(div)

arithmetic(x,y)
