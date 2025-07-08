'''Problem Discription : I am provided co-ordinates (x,y,z) and I need to print only those permutation list who satisfy the 
                         condition i+j+k != n  (n is a another number provided)
                         link : https://www.hackerrank.com/challenges/list-comprehensions
                         
Approach : will apply for loops till the given no. for each coordinates to generate random no. and apply the condition and
             then print it'''


from itertools import permutations

x = int(input())
y = int(input())
z = int(input())
n = int(input())

lst = [[i, j, k] 
        for i in range(x+1)
        for j in range(y+1)
        for k in range(z+1)
        if i + j + k != n ]
print(lst)

#Time complexity : O(x*y*z)
