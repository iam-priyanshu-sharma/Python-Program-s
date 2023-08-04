# Function to extract even and odd numbers from the list
def extract_even_odd(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    odd_numbers = [num for num in lst if num % 2 != 0]
    return even_numbers, odd_numbers


# Declare a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Extract even and odd numbers from the list
even_list, odd_list = extract_even_odd(my_list)

# Print the results
print("Original list:", my_list)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
