# Function to append elements to the list
def append_elements(lst, num_elements):
    for i in range(num_elements):
        element = int(input(f"Enter element {i + 1}: "))
        lst.append(element)


# Function to print the list elements
def print_list(lst):
    print("List elements:")
    for element in lst:
        print(element)


# List Created
my_list = []
num_elements = int(input("Enter the number of elements you want to add: "))
append_elements(my_list, num_elements)  # Function call
print_list(my_list)
