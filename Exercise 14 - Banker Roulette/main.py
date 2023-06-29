import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_of_items = len(names)
random_choice = random.randint(0, num_of_items - 1)
person_who_will_buy = names[random_choice]

print(person_who_will_buy + " is going to buy the meal today!")
