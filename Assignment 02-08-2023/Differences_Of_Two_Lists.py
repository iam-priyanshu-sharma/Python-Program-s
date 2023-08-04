# Function to find the differences between two lists
def find_differences(list1, list2):
    # Convert lists to sets to perform set operations
    set1 = set(list1)
    set2 = set(list2)

    # Find elements that are in list1 but not in list2
    difference_list1 = list(set1 - set2)

    # Find elements that are in list2 but not in list1
    difference_list2 = list(set2 - set1)

    return difference_list1, difference_list2


# Declare two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Find the differences between the two lists
diff_list1, diff_list2 = find_differences(list1, list2)

# Print the differences
print("Elements in list1 but not in list2:", diff_list1)
print("Elements in list2 but not in list1:", diff_list2)
