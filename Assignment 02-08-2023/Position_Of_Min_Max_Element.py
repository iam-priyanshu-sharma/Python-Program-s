def find_min_max_positions(lst):
    if not lst:
        return None, None

    min_pos = lst.index(min(lst))
    max_pos = lst.index(max(lst))
    return min_pos, max_pos


# Declare a list
my_list = [10, 30, 20, 40, 50, 30]

# Find the positions of the minimum and maximum elements
min_position, max_position = find_min_max_positions(my_list)

# Print the results
if min_position is not None and max_position is not None:
    print(f"Position of the minimum element: {min_position}")
    print(f"Position of the maximum element: {max_position}")
else:
    print("The list is empty.")
