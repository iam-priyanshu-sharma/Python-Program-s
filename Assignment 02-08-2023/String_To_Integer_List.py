# Input a string of comma-separated integers
input_str = input("Enter comma-separated integers: ")

# Convert the input string into a list of integers
int_list = [int(num) for num in input_str.split(',')]

# Print the list of integers
print("List of integers:", int_list)
