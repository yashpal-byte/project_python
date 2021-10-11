"""there are 2 types of conversion: implicit conversion and explicit conversion. implicit conversion is done automatically by python interpreter to avoid data loss.
explicit type conversion also called typecasting which is forcefully done by the user"""
#code to convert integer type to hexadecimal, octal, binary
print("This program is to convert integer number to hexadecimal, octal, binary")
print("sample deaf program") 
int_num = 45
hexa = hex(int_num)
octa = oct(int_num)
binary = bin(int_num)
print(int_num, "this is hexadecimal: ",hexa, end=', ')
print("this is octal: ",octa, end=' ')
print("this is binary: ", binary)
print("--------------------------------------------------------")
print("string formatting example")
print(f"hexadecimal: {hexa}, octal: {octa}, binary: {binary}")

#########################################
print("user input")
int_input= int(input('Enter a integer value: '))
hexad = hex(int_input)
octat = oct(int_input)
binary1 = bin(int_input)
print(int_input, "this is hexadecimal: ",hexad, end=', ')
print("this is octal: ",octat, end=' ')
print("this is binary: ", binary1)
print("--------------------------------------------------------")
print("string formatting example")
print(f"hexadecimal: {hexad}, octal: {octat}, binary: {binary1}")

