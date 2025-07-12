'''Problem Statement : I am provided list of countery stamps one by one, i need to count the total no. of distinct country stamps
                       , easy right....
                       Link : https://www.hackerrank.com/challenges/py-set-add
                       
Approach : i create a empty list, and append the country stamps using add() input and in the end print the length of the set
'''
A_size = int(input())
A = set()
for i in range(A_size):     #O(n)
    x = input()
    A.add(x)

print(len(A))               #O(1)

#Time Complexity : O(n)
#Space Complexity : O(n)  
