def remove_elements_in_range(lst, start_index, end_index):
    # Using list slicing to remove elements in the specified range
    lst = lst[:start_index] + lst[end_index + 1:]
    return lst


# Declare a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Range of elements to remove (start_index inclusive, end_index inclusive)
start_index = 2
end_index = 5

# Removing elements in the specified range
my_list = remove_elements_in_range(my_list, start_index, end_index)

# Print the updated list
print("List after removing elements in the specified range:", my_list)
