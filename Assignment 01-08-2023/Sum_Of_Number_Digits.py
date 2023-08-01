def get_digit_sum(number):
    return sum(int(digit) for digit in str(number))


my_list = [123, 45, 6789]

sum_of_digits = sum(get_digit_sum(number) for number in my_list)

print("Sum of digits in the list:", sum_of_digits)
