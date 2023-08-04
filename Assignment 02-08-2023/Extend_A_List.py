# Method 1: Using extend() method
original_list = [1, 2, 3]
new_elements = [4, 5, 6]
original_list.extend(new_elements)
print("Method 1:", original_list)

# Method 2: Using += operator
original_list = [1, 2, 3]
new_elements = [4, 5, 6]
original_list += new_elements
print("Method 2:", original_list)

# Method 3: Using list concatenation
original_list = [1, 2, 3]
new_elements = [4, 5, 6]
original_list = original_list + new_elements
print("Method 3:", original_list)

# Method 4: Using for loop
original_list = [1, 2, 3]
new_elements = [4, 5, 6]
for element in new_elements:
    original_list.append(element)
print("Method 4:", original_list)

# Method 5: Using insert() method
original_list = [1, 2, 3]
new_elements = [4, 5, 6]
for index, element in enumerate(new_elements):
    original_list.insert(index, element)
print("Method 5:", original_list)

# Method 6: Using list comprehension and extend()
original_list = [1, 2, 3]
new_elements = [4, 5, 6]
original_list.extend([element for element in new_elements])
print("Method 6:", original_list)
