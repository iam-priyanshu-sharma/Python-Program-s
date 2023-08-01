# using in
my_list = [1, 2, 3, 4, 5]
element = 3

if element in my_list:
    print("Element exists in the list")
else:
    print("Element does not exist in the list")

# using loop
my_list = [1, 2, 3, 4, 5]
element = 3

exists = False
for item in my_list:
    if item == element:
        exists = True
        break

if exists:
    print("Element exists in the list")
else:
    print("Element does not exist in the list")

# using count()
my_list = [1, 2, 3, 4, 5]
element = 3

if my_list.count(element) > 0:
    print("Element exists in the list")
else:
    print("Element does not exist in the list")
