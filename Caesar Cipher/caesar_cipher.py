from Art import logo


def caesar(directions, user_input, shift_amount):
    output_text = ""
    if directions == "encode":
        for char in user_input:
            if char in alphabet:
                output_text += alphabet[alphabet.index(char) + shift_amount - 26]
            else:
                output_text += char
        print(f"The encoded text is {output_text}")
    if directions == "decode":
        for char in user_input:
            if char in alphabet:
                output_text += alphabet[alphabet.index(char) - shift_amount]
            else:
                output_text += char
        print(f"The decoded text is {output_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

isContinue = True

print(logo)
while isContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(directions=direction, user_input=text, shift_amount=shift)
    choice = input("Do you want to continue? Yes or No:\n").lower()

    if choice == "no":
        isContinue = False
