def interchange_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]


my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

interchange_first_last(my_list)
print("List after interchange:", my_list)
