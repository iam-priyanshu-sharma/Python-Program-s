# Function to print the elements of the list
def print_list(lst):
    print("List elements:", lst)


# Function to find the maximum element in the list
def find_max(lst):
    max_element = max(lst)
    print("Maximum element:", max_element)


# Function to find the minimum element in the list
def find_min(lst):
    min_element = min(lst)
    print("Minimum element:", min_element)


# Function to calculate the sum of elements in the list
def calculate_sum(lst):
    total_sum = sum(lst)
    print("Sum of elements:", total_sum)


# Function to sort the list in ascending order
def sort_list(lst):
    sorted_list = sorted(lst)
    print("Sorted list (ascending order):", sorted_list)


# Function to reverse the list
def reverse_list(lst):
    reversed_list = list(reversed(lst))
    print("Reversed list:", reversed_list)


# Function to remove duplicates from the list
def remove_duplicates(lst):
    unique_list = list(set(lst))
    print("List after removing duplicates:", unique_list)


# Main program
my_list = [5, 3, 8, 1, 2, 7, 5, 4]

print_list(my_list)
find_max(my_list)
find_min(my_list)
calculate_sum(my_list)
sort_list(my_list)
reverse_list(my_list)
remove_duplicates(my_list)
