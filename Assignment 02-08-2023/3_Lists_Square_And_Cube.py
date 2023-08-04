# Function to generate squares of numbers
def generate_squares(numbers):
    return [num ** 2 for num in numbers]


# Function to generate cubes of numbers
def generate_cubes(numbers):
    return [num ** 3 for num in numbers]


# Create a list of numbers
numbers_list = [1, 2, 3, 4, 5]

# Generate squares and cubes of the numbers
squares_list = generate_squares(numbers_list)
cubes_list = generate_cubes(numbers_list)

# Print the three lists
print("Original Numbers List:", numbers_list)
print("Squares List:", squares_list)
print("Cubes List:", cubes_list)
