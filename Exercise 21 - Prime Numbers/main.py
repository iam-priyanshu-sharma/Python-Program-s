def prime_checker(number):
    if number > 1:
        for j in range(2, int(number / 2) + 1):
            if (number % j) == 0:
                print(f"{number} is not a prime number.")
                break
        else:
            print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
