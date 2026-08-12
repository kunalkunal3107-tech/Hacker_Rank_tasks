'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''

# first way to solve this

# def saw_ap(s):
#     return s.swapcase()


# if __name__ == "__main__":
#     s = input("enter")
#     # for ch in s :
#     print(saw_ap(s))

# second way to solve this 

# def saw(n):
#     result = ""

#     for ch in n:
#         if ch.islower():
#             result += ch.upper()

#         elif ch.isupper():
#             result += ch.lower()
#         else:
#             result += ch 
#     return result



# if __name__ == "__main__":
#     n = input("")
#     output = saw(n)
#     print(output)

# num= int(input("enter your number"))
# lis = []
# for i in range(num):
#     lis += i

# print(lis)
pip = '''kunal is the hero in there file and also there family life'''
fil = open("superman.txt","w")
fil.write(pip)
fil.close()