def split_into_two_halves(lst):
    middle_index = len(lst) // 2
    first_half = lst[:middle_index]
    second_half = lst[middle_index:]

    return first_half, second_half


# Declare the original list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", original_list)

# Split the original list into two halves
first_half_list, second_half_list = split_into_two_halves(original_list)

# Print the two halves
print("First half list:", first_half_list)
print("Second half list:", second_half_list)
