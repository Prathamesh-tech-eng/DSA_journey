'''Problem Description : I am provided with two sets, and I need to print elements that are not common in both sets
                         e.g : A = {1,2,3,4} B = {5,3,2,7}   O/p : {1,4,5,7}
                         Link : https://www.hackerrank.com/challenges/symmetric-difference
                         
Approach : Python comes with a built in set operation, i.e exclusive, I will use it and print the result'''

A_size = int(input())
A = set(map(int,input().split()))    #O(n)
B_size = int(input())
B = set(map(int,input().split()))    #O(m)

C = list(A ^ B)                      #Symmetric Difference : O(n + m)
C.sort()                             #Sorting : O(klogk)  k = len(C)
for items in C:                      #O(n)
    print(items)


#Time Complexity : O(n + m + klogk) = O(n + m)log(n + m)
#Space Complexity : O(n + m)