# Function to swap two elements in a list
def swap_elements(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]


# Declare a list
my_list = [1, 2, 3, 4, 5]

# Indices of elements to swap
index1 = 1
index2 = 3

# Before swap
print("Original list:", my_list)

# Swap the elements
swap_elements(my_list, index1, index2)

# After swap
print("List after swapping elements:", my_list)
