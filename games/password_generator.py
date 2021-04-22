import random

"""Pypassword generator"""
print("Welcome to the PyPassword Generator!")
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_numbers = '0123456789'
letters = list(ascii_letters)
numbers = list(ascii_numbers)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
symbols_letters_numbers = symbols + letters + numbers

total_letters = int(input("How many letters would you like in your password? "))
total_symbols = int(input("How many symbols would you like? "))
total_numbers = int(input("How many numbers would you like? "))
total_length = total_letters + total_symbols + total_numbers

password = ""
for char in range(total_length+1):
    password += random.choice(symbols_letters_numbers)

print(f"Here is your password: {password}")