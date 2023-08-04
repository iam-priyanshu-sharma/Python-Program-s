# Function to check if all elements in a list are unique
def are_all_elements_unique(lst):
    return len(set(lst)) == len(lst)


# Test cases
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 3, 4, 5]
list3 = []

print("List 1: Are all elements unique?", are_all_elements_unique(list1))
print("List 2: Are all elements unique?", are_all_elements_unique(list2))
print("List 3: Are all elements unique?", are_all_elements_unique(list3))
