# Function to interchange first and last elements of a list
def interchange_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]


# Declare a list
my_list = [1, 2, 3, 4, 5]

# Before interchange
print("Original list:", my_list)

# Interchange first and last elements
interchange_first_last(my_list)

# After interchange
print("List after interchanging first and last elements:", my_list)
