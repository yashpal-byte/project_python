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
#########################################
#so far we have done using int to other form of numbers
#now we will covert among different types
binnum = int(input(),2) #TO INPUT BINARY, OCTAL OR HEXADECIMAL NUMBER FROM USER.. IT HAS TO BE DONE BY INT() BY USING BASE ARGUMENT IN INT(). PYTHON PROVIDES 0 AND 2-36 BASE SYSTEMS
intgr = int(binnum)
hexd = hex(binnum)
octal = oct(binnum)
print(binnum, intgr,hexd,octal)

#############################################





