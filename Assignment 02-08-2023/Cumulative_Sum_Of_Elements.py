# Function to calculate the cumulative sum of elements in a list
def cumulative_sum(lst):
    cumulative_sum_list = []
    total = 0

    for num in lst:
        total += num
        cumulative_sum_list.append(total)

    return cumulative_sum_list


# Declare a list
my_list = [1, 2, 3, 4, 5]

# Calculate the cumulative sum
cumulative_sum_list = cumulative_sum(my_list)

# Print the cumulative sum list
print("Original list:", my_list)
print("Cumulative sum list:", cumulative_sum_list)
