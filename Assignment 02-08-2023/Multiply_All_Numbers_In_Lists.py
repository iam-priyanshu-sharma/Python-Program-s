# Function to multiply all numbers in a list using a loop
def multiply_list_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result


# Declare a list
my_list = [1, 2, 3, 4, 5]
print("List:",my_list)

# Multiply all numbers in the list using a loop
product = multiply_list_elements(my_list)

# Print the result
print("Product of all numbers:", product)
