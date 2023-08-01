def swap_elements(lst, pos1, pos2):
    if 0 <= pos1 < len(lst) and 0 <= pos2 < len(lst):
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]


user_input = input("Enter strings separated by spaces: ")
my_list = user_input.split()

print("Original List:", my_list)

pos1 = int(input("Enter the position of the first element to swap: "))
pos2 = int(input("Enter the position of the second element to swap: "))

swap_elements(my_list, pos1, pos2)
print("List after swapping:", my_list)
