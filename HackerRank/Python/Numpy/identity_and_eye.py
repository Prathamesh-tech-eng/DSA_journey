'''Problem Description : I am provided with dimension of an 2D array , and I need to print an identity matrix of respective dimension
                         e.g : 2 2  O/P : [[1 0]
                                           [0 1]]
                         Link : https://www.hackerrank.com/challenges/np-eye-and-identity
                         
Approach : I will use np.eye to print identity matrix of given dimension, could have used np.identity but it will only print square matrix
'''
import numpy as np
np.set_printoptions(legacy='1.13')
N, M = map(int, input().split())
print(np.eye(N,M,k=0))

#Time Complexity : O(N * M)
#Space Complexity : O(N * M)