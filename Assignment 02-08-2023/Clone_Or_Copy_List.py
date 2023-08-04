import copy

# Using slice notation [:]
# Declare the original list
original_list = [1, 2, 3, 4, 5]

# Create a shallow copy of the list using slice notation
shallow_copy = original_list[:]

# Modify the original list to demonstrate the difference
original_list[0] = 10

# Print the original list and the shallow copy
print("Original list:", original_list)
print("Shallow copy:", shallow_copy)

# Using list() method
# Declare the original list
original_list = [1, 2, 3, 4, 5]

# Create a shallow copy of the list using the list() constructor
shallow_copy = list(original_list)

# Modify the original list to demonstrate the difference
original_list[0] = 10

# Print the original list and the shallow copy
print("Original list:", original_list)
print("Shallow copy:", shallow_copy)

# Using copy() method from copy modeule
# Declare the original list
original_list = [1, 2, 3, 4, 5]

# Create a deep copy of the list using the copy() method
deep_copy = copy.copy(original_list)

# Modify the original list to demonstrate the difference
original_list[0] = 10

# Print the original list and the deep copy
print("Original list:", original_list)
print("Deep copy:", deep_copy)
