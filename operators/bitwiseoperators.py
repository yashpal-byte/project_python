binary1 = int(input('binary1: '),base=2)
binary2 = int(input('binary2: '),base=2)
complement1 = ~binary1
complement2 = ~binary2
bitwise = binary1 & binary2
bitwise2 = binary2 & binary1
bitwise3 = binary1 & binary1
bitwise4 = binary1 | binary2
bitwise5 = binary2 | binary1
bitwise6 = binary1 ^ binary2
print("bitwise",bitwise)
print("bitwise2",bitwise2)
print("bitwise3",bitwise3)
print("bitwise4",bitwise4)
print("bitwise5",bitwise5)
print("bitwise6",bitwise6)
print('complement1',complement1)
print('complement2',complement2)