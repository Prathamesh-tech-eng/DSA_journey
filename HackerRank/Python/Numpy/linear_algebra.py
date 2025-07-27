'''Problem Description : I am provided a matrix and I need to return determinant of the matrix.
                         Link : https://www.hackerrank.com/challenges/np-linear-algebra
                         
Approach : I will use the built in numpy, i.e np.linalg.det to find the determinant of the provided matirx.
'''

import numpy as np

N = int(input())

A = np.array([list(map(float, input().split())) for _ in range(N)])

print(f"{round(np.linalg.det(A),2)}")

#Time Complexity : O(N^3)
#Space Complexity : O(N^2)