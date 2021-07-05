new_list = [1, 2, 3] # the values are not stored in memory, instead the values 1,2,3 are stored elsewhere
                     # in memory and the array stores references to each of those objects
result = new_list[0]
if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        break