def swap_elements(lst, index1, index2):
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        lst[index1], lst[index2] = lst[index2], lst[index1]


my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

swap_elements(my_list, 1, 3)
print("List after swapping elements:", my_list)
