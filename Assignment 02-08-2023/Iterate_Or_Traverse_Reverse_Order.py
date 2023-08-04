# Using reversed() function

# Declare a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traverse the list in reverse order using reversed()
for element in reversed(my_list):
    print(element)


# Using negative indices

# Traverse the list in reverse order using negative indices
for i in range(len(my_list)-1, -1, -1):
    print(my_list[i])
