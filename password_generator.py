import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
numbers = "123456789"
special_char = "~!@#$%^&*()_-+=}{[]|\;:""''<>,.?/"

upper , lower , number , special = True , True , True , True

all = ''

if upper:
    all +=  uppercase
if lower:
    all += lowercase 
if number:
    all += numbers 
if special:
    all += special_char

print()
length = int(input("Enter the length of the Password  :"))
amount = 10 

for i in range(amount):
    password = "".join(random.sample(all, length))
    print(password)