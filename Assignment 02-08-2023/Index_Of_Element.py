# Using index() method
# Function to find the index of an item in a list using the index() method
def find_index_using_index(lst, item):
    try:
        index = lst.index(item)
        return index
    except ValueError:
        return None


# Declare a list
my_list = [10, 20, 30, 40, 50]

# Item to find
item_to_find = 30

# Find the index using index() method
index = find_index_using_index(my_list, item_to_find)

# Print the result
print(f"Index of {item_to_find} in the list:", index)


# Using list comprehension
# Function to find the index of an item in a list using a list comprehension
def find_index_using_list_comprehension(lst, item):
    indices = [index for index, value in enumerate(lst) if value == item]
    return indices


# Declare a list
my_list = [10, 20, 30, 40, 50, 30]

# Item to find
item_to_find = 30

# Find the index using list comprehension
indices = find_index_using_list_comprehension(my_list, item_to_find)

# Print the result
print(f"Indices of {item_to_find} in the list:", indices)
