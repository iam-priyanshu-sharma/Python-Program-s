def remove_duplicates(lst):
    # Convert the list to a set to remove duplicates
    unique_elements = set(lst)

    # Convert the set back to a list
    lst_without_duplicates = list(unique_elements)

    return lst_without_duplicates


# Declare a list with duplicate elements
my_list = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicate elements from the list
my_list_without_duplicates = remove_duplicates(my_list)

# Print the list without duplicates
print("List without duplicates:", my_list_without_duplicates)
