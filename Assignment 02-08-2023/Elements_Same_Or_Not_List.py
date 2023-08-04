# Function to check if all elements of a list are the same
def are_all_elements_same(lst):
    if len(lst) == 0:
        return True
    return all(element == lst[0] for element in lst)


# Test cases
list1 = [1, 1, 1, 1, 1]
list2 = [1, 2, 1, 1, 1]
list3 = []

print("List 1: Are all elements same?", are_all_elements_same(list1))
print("List 2: Are all elements same?", are_all_elements_same(list2))
print("List 3: Are all elements same?", are_all_elements_same(list3))
