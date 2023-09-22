import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
password_letters = int(input("How many letters would you like in your password? \n"))
password_symbols = int(input("How many symbols would you like? \n"))
password_nums = int(input("How many numbers? \n"))

random_chars = []
new_password = ""

for char in range(0, password_letters):
    random_chars.append(random.choice(letters))

for char in range(0, password_symbols):
    random_chars.append(random.choice(symbols))

for char in range(0, password_nums):
    random_chars.append(random.choice(numbers))

random.shuffle(random_chars)

for char in random_chars:
    new_password += char

print(new_password)