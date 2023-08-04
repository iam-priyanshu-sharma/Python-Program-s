def separate_even_odd(lst):
    even_numbers = []
    odd_numbers = []

    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers


# Declare a list with both even and odd numbers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Separate even and odd numbers into two lists
even_list, odd_list = separate_even_odd(my_list)

# Print the results
print("Original list:", my_list)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
