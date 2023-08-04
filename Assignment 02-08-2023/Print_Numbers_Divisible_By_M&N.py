def find_divisible_numbers(lst, m, n):
    divisible_numbers = [num for num in lst if num % m == 0 and num % n == 0]
    return divisible_numbers


# Declare a list of numbers
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Define two numbers M and N
M = 2
N = 4

# Find numbers divisible by M and N in the list
result_list = find_divisible_numbers(my_list, M, N)

# Print the result
print(f"Numbers divisible by {M} and {N} are:", result_list)
