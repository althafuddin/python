
import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+{}|<>?,./;'[]\=-`"
pwd_length = int(input("What is the lenght of your pwd:"))
pwd_number = int(input("How many passwords do you want:"))


for n in range(pwd_number):
    pwd_string = ""
    for number in range(pwd_length):
        pwd_string += random.choice(char)
    print(pwd_string)
