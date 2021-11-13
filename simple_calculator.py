#simple arithmetic calculator
print()
print("*****simple calculator*****")
print("""
********Options********
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Floor division
        6. Exponential
        7. Mod operation
        """)
option = input("Enter number corresponding to option ")

print(f"you have chosen {option}")

if (option == '1') or (option == '2') or (option == '3') or (option == '4') or (option == '5') or (option == '6') or (option == '7'):
    print("Enter 2 numbers")
    a = int(input("Enter a number "))
    b = int(input("Enter a number "))
    if option == '1':
        #addition
        add = a + b
        print(add)
    elif option == '2':
        #subtraction
        sub = a - b
        print(sub)
    elif option == '3':
        #multiplication
        multiply = a * b
        print(multiply)
    elif option == '4':
        #division
        div = a/b
        print(div)
    elif option == '5':
        #integer division or floor division
        fdiv = a//b
        print(fdiv)
    elif option == '6':
        #exponential
        expo = a**b
        print(expo)
    elif option == '7':
        #mod
        mod = a%b
        print(mod)
    
    print("chosen arithmetic operation has executed successfully")
else:
    print("You didn't choose valid number")

#####
