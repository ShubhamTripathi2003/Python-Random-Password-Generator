#Developed By Jagdamba Tripathi

import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits  
PUNCTUATION = string.punctuation    

length = int(input("How long do you want your password: "))
want_digits = input("Want digits ? (Yes or No) : ")
want_letters = input("Want letters ? (Yes or No): ")
want_puncts = input("Want punctuation ? (Yes or No): ")

if want_digits.lower()=="no":
        printable = f'{LETTERS}{PUNCTUATION}'
elif want_letters.lower()=="no":
        printable = f'{NUMBERS}{PUNCTUATION}'
elif want_puncts.lower()=="no":
        printable = f'{LETTERS}{NUMBERS}'
else:
        printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

printable = list(printable)
random.shuffle(printable)

random_password = random.choices(printable, k=length)
random_password = ''.join(random_password)
print("Your Password Is :",random_password)
