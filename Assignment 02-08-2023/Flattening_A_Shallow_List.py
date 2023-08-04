# Function to flatten a shallow list using list comprehension
def flatten_list_using_comprehension(lst):
    return [element for sublist in lst for element in sublist]


# Declare a shallow list
shallow_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

# Flatten the shallow list using list comprehension
flattened_list = flatten_list_using_comprehension(shallow_list)

# Print the flattened list
print("Original shallow list:", shallow_list)
print("Flattened list using comprehension:", flattened_list)
