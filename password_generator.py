#!/usr/bin/python3

import random

# Defining my lists
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'
]

password = ''

# banner
banner = '''
                                 _                            _
 ___ ___ ___ ___ _ _ _ ___ ___ _| |   ___ ___ ___ ___ ___ ___| |_ ___ ___ 
| . | .'|_ -|_ -| | | | . |  _| . |  | . | -_|   | -_|  _| .'|  _| . |  _|
|  _|__,|___|___|_____|___|_| |___|  |_  |___|_|_|___|_| |__,|_| |___|_|  
|_|                                  |___|                                
Version: 1
[+] Developped by W4RSH3LL [+]
'''
print(banner)

# Taking user input
nb_letters = int(input("How many letters do you wish to have in your password > "))
nb_number = int(input("How many number do you wish to have in your password > "))
nb_symbols = int(input("How many symbols do you wish to have in your password > "))

# Defining our 3 lists
password_letter_list = []
password_number_list = []
password_symbol_list = []

# Creating 3 random char lists and appending them to our password_lists

# Generating our letter list
for letter in range(0, nb_letters):
    letter = random.choice(letters)
    password_letter_list.append(letter)

# Generating our number list
for number in range(0, nb_number):
    number = random.choice(numbers)
    password_number_list.append(number)

# Generating our symbol list
for symbol in range(0, nb_symbols):
    symbol = random.choice(symbols)
    password_symbol_list.append(symbol)

# Combining all the chars of a list
every_char_list = password_letter_list + password_number_list + password_symbol_list

# Adding a random shuffle
random.shuffle(every_char_list)

# Joining all characters
password = ''.join(every_char_list)

# Output
print(f'Your password will be : {password}')