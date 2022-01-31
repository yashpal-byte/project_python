#arithmetic operators
#+ --> addition (unary and binary operator)
#- --> subtraction (unary and binary operator)
#* --> multiplication
#** --> exponential
#/ --> division
#// --> floor division
#% --> modulus
#########################################################

a = int(input('enter a number: ')) #input from user
b = int(input('enter a number: ')) #input from user
print('addition--',a+b) #add.
print('subtraction--',a-b) #subtract.
print('multiplication--', a*b) #multiply
print('division--',a/b) #division. returns float number regardless of data type
print('exponential--',a**b) #exponent
print('floor division--',a//b) #floor division. returns int if both operands are int, returns float if any of the operand is float. rounds the value to the lesser value of the quotient
print('modulus--',a%b) #returns remainder. but behaves differently with negative numbers                                .

