'''Problem Description : I am provided two arrays each with size n*p and m*p and I need to concatenate them along axis = 0
                         link : https://www.hackerrank.com/challenges/np-concatenate
                         
Approach : I will use numpy.concatenate() to achieve concatenation.
'''

import numpy as np

n, m, p = (map(int, input().split()))

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]

A = np.array(A)
B = np.array(B)
A.shape = (n, p)
B.shape = (m, p)
print(np.concatenate((A,B), axis = 0))

#Time Complexity : O((n + m)*p)
#Space Complexity : O((n + m)*p)