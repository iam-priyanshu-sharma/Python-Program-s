# Using in keyword
# Function to check if an element is present in the list using 'in' keyword
def is_element_present_using_in(lst, element):
    return element in lst


# Declare a list
my_list = [1, 2, 3, 4, 5]

# Element to check
element_to_check = 3

# Check if the element is present in the list using 'in' keyword
result = is_element_present_using_in(my_list, element_to_check)

# Print the result
print(f"Element {element_to_check} is present in the list: {result}")


# Using index() method
# Function to check if an element is present in the list using 'index()' method
def is_element_present_using_index(lst, element):
    try:
        lst.index(element)
        return True
    except ValueError:
        return False


# Declare a list
my_list = [1, 2, 3, 4, 5]

# Element to check
element_to_check = 6

# Check if the element is present in the list using 'index()' method
result = is_element_present_using_index(my_list, element_to_check)

# Print the result
print(f"Element {element_to_check} is present in the list: {result}")
