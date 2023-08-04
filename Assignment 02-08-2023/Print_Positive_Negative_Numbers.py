# Function to print positive and negative numbers from a list
def print_positive_negative_numbers(lst):
    positive_numbers = [num for num in lst if num > 0]
    negative_numbers = [num for num in lst if num < 0]

    print("Positive numbers:", positive_numbers)
    print("Negative numbers:", negative_numbers)


# Declare a list
my_list = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
print("Original List:", my_list)

# Print positive and negative numbers from the list
print_positive_negative_numbers(my_list)
