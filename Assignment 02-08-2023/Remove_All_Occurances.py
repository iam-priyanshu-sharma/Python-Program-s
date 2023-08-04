def remove_all_occurrences(lst, element_to_remove):
    # Using a while loop to remove all occurrences of the element
    while element_to_remove in lst:
        lst.remove(element_to_remove)


# Declare a list
my_list = [1, 2, 3, 4, 3, 5, 6, 2, 5, 11, 1, 4]

# Element to remove
element_to_remove = 3

# Removing all occurrences of the element
remove_all_occurrences(my_list, element_to_remove)

# Print the updated list
print("List after removing all occurrences:", my_list)
