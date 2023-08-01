# using clear()
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)

# using pop()
my_list = [1, 2, 3, 4, 5]
while my_list:
    my_list.pop()
print(my_list)

# using slicing
my_list = [1, 2, 3, 4, 5]
my_list[:] = []
print(my_list)
