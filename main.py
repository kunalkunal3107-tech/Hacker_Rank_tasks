# s= ""
# for ch in "abc":
#     s = ch + s
# print(s)
# cba

# set a size M = 4
a = {2, 4, 5, 9}
# set b size N = 4
b = {2, 4, 11, 12}
c = a.difference(b)
d = b.difference(a)
print(a,b,c,d,end="")