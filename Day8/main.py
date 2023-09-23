from art import logo

def caesar(text: str, shift: int, direction: str):

    message = ""

    for char in text:

        if char not in alphabet:
            # Keep the same character in the message
            message += char
            continue
        else:
            i = alphabet.index(char)

        if direction == "encode":
            if i + shift > 25:
                message += alphabet[i + (shift % 26)]
            else:
                message += alphab1et[i + shift]
        elif direction == "decode":
            if i - shift < 0:
                message += alphabet[i - (shift % 26)]
            else:
                message += alphabet[i - shift]
    
    print(message)


is_running = True

while is_running:

    print(logo)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    while True:
        do_restart = input("Type 'yes' if you want to go again. Otherwise type 'no'").lower()

        if do_restart == "yes":
            break
        elif do_restart == "no":
            is_running = False
            break
        else:
            print("please pick a valid option.")
