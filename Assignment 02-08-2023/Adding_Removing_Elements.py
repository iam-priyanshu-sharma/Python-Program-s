# Declare an empty list
my_list = []

# Adding elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print("List after adding elements:", my_list)

# Removing element from the list using remove()
my_list.remove(2)

# Removing element from the list using pop()
index_to_remove = 1
my_list.pop(index_to_remove)  # Remove the element at index 1 (value 3)

print("List after removing elements:", my_list)
