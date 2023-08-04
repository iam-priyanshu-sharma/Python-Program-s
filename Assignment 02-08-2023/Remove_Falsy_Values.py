# Function to remove falsy values from the list
def remove_falsy(lst):
    filtered_list = [value for value in lst if value]
    return filtered_list


# Declare a list with falsy values
my_list = [0, False, '', None, [], 1, True, 'hello', [1, 2, 3]]

# Remove falsy values from the list
cleaned_list = remove_falsy(my_list)

# Print the cleaned list
print("Original list:", my_list)
print("List after removing falsy values:", cleaned_list)
