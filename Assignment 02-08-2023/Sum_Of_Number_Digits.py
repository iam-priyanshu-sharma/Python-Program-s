# Function to find the sum of the digits of a number
def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


# Function to find the sum of digits in a list
def sum_of_digits_in_list(lst):
    total_sum = 0
    for num in lst:
        total_sum += sum_of_digits(num)
    return total_sum


# Declare a list of numbers
my_list = [123, 456, 789]

# Find the sum of digits in the list
result = sum_of_digits_in_list(my_list)

# Print the result
print("List of numbers:", my_list)
print("Sum of digits in the list:", result)
