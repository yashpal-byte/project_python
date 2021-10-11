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

