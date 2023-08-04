# Function to find the index of the first matched element in a list
def find_first_match_index(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index
    return None  # Return None if the target element is not found


# Declare a list
my_list = [10, 20, 30, 40, 30, 50, 10, 40, 20, 50, 20]

# Element to find
target_element = 30

# Find the index of the first matched element
index = find_first_match_index(my_list, target_element)

# Print the result
if index is not None:
    print(f"The first occurrence of {target_element} is at index {index}.")
else:
    print(f"{target_element} is not found in the list.")
