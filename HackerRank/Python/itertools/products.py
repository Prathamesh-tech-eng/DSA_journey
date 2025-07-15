'''Problem Description : I am given two lists and I need to find the cartesian product of two of them
                         e.g : A : [1,2]  B : [22,33]  A*B = [(1,22), (1,33), (2,22), (2,33)]
                         Link : https://www.hackerrank.com/challenges/itertools-product
                          
Approach : I will use the built in functions itertools.product() to find the cartesian product
 '''

import itertools
A, B = (list(map(int, input().split())) for _ in range(2))
for i in itertools.product(A,B):
    print(i, end=" ")

#Time Complexity : O(m*n)  where m = len(A) and n = len(B)
#Space Complexity : O(m + n)