'''
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.
'''
# Python Code (Easy Version - Beginners)
def check(uid):

    if len(uid) != 10:
        return False
    
    upper = 0
    digit = 0

    for us in uid:
        if us.isupper():
            upper +=1
        if us.isdigit():
            digit +=1
        if not us.isalnum():
            return False
    if upper<2:
        return False
    if digit<3:
        return False
    if len(uid) !=10:
        return False
    return True


t = int(input("Enter the number"))
for _ in range(t):
    uid = input("Enter Id")

    if check(uid):
        print("Valid")
    else:
        print("Invaild")

# Regex Solution (Expected by HackerRank)

import re

for _ in range(int(input())):
    uid = input()

    if (
        re.search(r"[A-Z].*[A-Z]", uid)
        and len(re.findall(r"\d", uid)) >= 3
        and re.match(r"^[A-Za-z0-9]{10}$", uid)
        and len(set(uid)) == 10
    ):
        print("Valid")
    else:
        print("Invalid")