#82. Python program to calculate the sum of all items of a container (tuple, list, set, dictionary)
lst = [1,2,3,4,5]
tup = 1,2,3,4,5
set_ = {1,2,3,4,5}

sum_lst = 0
for i in lst:
    sum_lst = sum_lst + i

sum_tup = 0
for i in tup:
    sum_tup = sum_tup + i

sum_set = 0
for i in set_:
    sum_set = sum_set + i

print(sum_lst)
print(sum_tup)
print(sum_set)