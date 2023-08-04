import heapq


# Function to find N largest and smallest elements from a list
def find_n_largest_and_smallest(lst, N):
    largest_elements = heapq.nlargest(N, lst)
    smallest_elements = heapq.nsmallest(N, lst)
    return largest_elements, smallest_elements


# Declare a list
my_list = [10, 4, 8, 3, 7, 6, 5, 9, 2, 1]

# Specify the value of N
N = 3

# Find N largest and smallest elements
largest_elements, smallest_elements = find_n_largest_and_smallest(my_list, N)

# Print the results
print(f"{N} Largest elements: {largest_elements}")
print(f"{N} Smallest elements: {smallest_elements}")
