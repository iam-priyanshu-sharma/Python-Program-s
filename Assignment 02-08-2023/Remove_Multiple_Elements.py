# Using List Comprehension

# Declare the original list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Elements to remove from the list
elements_to_remove = [2, 4, 6]

# Remove multiple elements using list comprehension
filtered_list = [element for element in my_list if element not in elements_to_remove]

# Print the filtered list
print("Filtered list:", filtered_list)

# Using remove()

# Declare the original list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Elements to remove from the list
elements_to_remove = [2, 4, 6]

# Remove multiple elements using a loop and remove() method
for element in elements_to_remove:
    while element in my_list:
        my_list.remove(element)

# Print the updated list
print("Updated list:", my_list)
