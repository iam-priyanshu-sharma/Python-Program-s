# Function to remove empty lists from a list of lists
def remove_empty_lists(list_of_lists):
    non_empty_lists = [sublist for sublist in list_of_lists if sublist]
    return non_empty_lists


# Declare a list of lists
list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]

# Remove empty lists from the list of lists
cleaned_list = remove_empty_lists(list_of_lists)

# Print the cleaned list of lists
print("Original list of lists:", list_of_lists)
print("List of lists after removing empty lists:", cleaned_list)
