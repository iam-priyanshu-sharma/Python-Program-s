# Function to check if a list is empty
def is_list_empty(lst):
    if not lst:
        return True
    else:
        return False


# Declare an empty list
empty_list = []

# Declare a non-empty list
non_empty_list = [1, 2, 3]

# Check if the lists are empty
print("Is empty_list empty?", is_list_empty(empty_list))
print("Is non_empty_list empty?", is_list_empty(non_empty_list))
