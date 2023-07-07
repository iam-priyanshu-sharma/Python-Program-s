from art import logo


def caesar(start_text, shift_amount, cipher_direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char.isalpha():
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's the {cipher_direction}d result: {cipher_text}")


print(logo)

should_end = True

while should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_end = False
        print("Goodbye")
