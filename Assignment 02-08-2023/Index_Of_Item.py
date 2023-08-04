# Using index() method

# Declare a list
my_list = [10, 20, 30, 40, 50]

# Item to find
item_to_find = 30

# Find the index of the item using index() method
index = my_list.index(item_to_find)

# Print the result
print(f"The index of {item_to_find} is {index}.")

# Using Loop
# Declare a list
my_list = [10, 20, 30, 40, 50]

# Item to find
item_to_find = 30

# Find the index of the item using a loop
index = None
for i in range(len(my_list)):
    if my_list[i] == item_to_find:
        index = i
        break

# Print the result
if index is not None:
    print(f"The index of {item_to_find} is {index}.")
else:
    print(f"{item_to_find} is not found in the list.")

