from random import choice
len=12
valid_chars_for_Passwords="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*+-*/?"
#choice will select a random character from the string

password=[]
for each_char in range(len):
    password.append(choice(valid_chars_for_Passwords))
password="".join(password)
print(password)