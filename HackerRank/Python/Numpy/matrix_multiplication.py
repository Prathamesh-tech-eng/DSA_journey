'''Problem Description : I am provided two square matrix and I need to perform matrix multiplication and print the result.
                         link : https://www.hackerrank.com/challenges/np-dot-and-cross
                         
Approach : I will use np.dot() '''

import numpy as np

N = int(input())

A = np.array([list(map(int, input().split())) for _ in range(N)])
B = np.array([list(map(int, input().split())) for _ in range(N)])

print(np.dot(A,B))

#Time Complexity : O(N^3)
#Space Complexity : O(N^2)

