'''
Let's learn about list comprehensions! You are given three integers  
and  representing the dimensions of a cuboid along with an integer . 
Print a list of all possible coordinates given by  on a 3D grid where 
the sum of  is not equal to . Here, . Please use list comprehensions 
rather than multiple loops, as a learning exercise.
'''
# is [1,1,2,3,]

x = int(input())
y = int(input())
z = int(input())
n = int(input())



lis = [

    [i,j,k]
    for i in range(0,x+1)
    for j in range(0,y+1)
    for k in range(0,z+1)
    if i + j + k !=n
   
]

print(lis) # output is [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]