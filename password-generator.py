import string
import random

def gen():
    s1 = string.ascii_uppercase
    s4 = string.ascii_lowercase
    s2 = string.digits
    s3 = string.punctuation

    passlen = int(input("Enter password length: "))   # takes input from user

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)       #shuffles the list

    password = ("".join(s[0:passlen]))           # create a password of the required length
    print(password)

gen()