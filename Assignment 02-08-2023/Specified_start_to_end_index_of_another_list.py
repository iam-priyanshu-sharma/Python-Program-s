# Function to create a new list from a specified start to end index of another list
def create_sublist(original_list, start_index, end_index):
    return original_list[start_index:end_index + 1]


# Declare the original list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Specify the start and end index
start_index = 2
end_index = 6

# Create a new sublist from the original list
new_list = create_sublist(original_list, start_index, end_index)

# Print the new sublist
print("New sublist:", new_list)
