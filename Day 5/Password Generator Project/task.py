import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""
password = []

# for nr_letter in nr_letters:
# for letter in letters(range(nr_letters)):
for nr_letter in range(nr_letters):
    password += random.choice(letters)
for nr_symbol in range(nr_symbols):
    password += random.choice(symbols)
for nr_number in range(nr_numbers):
    password += random.choice(numbers)
# print(len(password))
# gen_pass = [password]
# gen_pass_length = len(gen_pass)
# print(gen_pass_length)
# password_length = len(password)

# for password_length in password:
#     gen_pass = [password_length]

    # password = random.choice(password_length)
    # print(password)
# for chars in gen_pass:
#     password = random.choice(gen_pass)
# print(random.choice(gen_pass))
# for chars in range(password_length):
#     password == password(chars)
print(password)
password_length = len(password)
print(password_length)
final_pass = ""
for char_count in range(password_length):
    password == random.shuffle(password)
for chars in password:
    final_pass += chars + ""

print("Your new password is: " + final_pass)
    # password = random.choice(nr_letters)
    # print(password)