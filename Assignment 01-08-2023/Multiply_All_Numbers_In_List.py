def multiply_list_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result


my_list = [1, 2, 3, 4, 5]

product = multiply_list_elements(my_list)

print("Product of all numbers in the list:", product)
