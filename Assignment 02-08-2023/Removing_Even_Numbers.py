# Declare the original list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use list comprehension to create a new list without even numbers
filtered_list = [num for num in my_list if num % 2 != 0]

# Print the new list without even numbers
print("List after removing even numbers:", filtered_list)
