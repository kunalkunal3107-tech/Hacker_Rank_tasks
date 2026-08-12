'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.
'''

n = int(input("enter number"))
arr = map(int, input("enter multi number").split())

li = list(arr)
st = set(li)
mx = max(st)
st.remove(mx)
kk = st
# st1 = set(li)
mx1 = max(kk)

print(mx1)