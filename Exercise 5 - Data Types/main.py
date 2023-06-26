two_digit_number = int(input("Type a two digit number: "))

sum_of_digits = two_digit_number / 10
sum_of_digits = sum_of_digits + two_digit_number % 10

print(int(sum_of_digits))
