'''Problem Description : I am provided with two arrays , I need to print there inner product and outer product.
                         Link : https://www.hackerrank.com/challenges/np-inner-and-outer
                         
Approach : I will use np.dot() for finding innerproduct and np.outer() for outer product
'''

import numpy as np

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

print(f"{np.dot(A, B)}\n{np.outer(A,B)}")

#Time Complexity : O(N^2)
#Space Complexity : O(N^2)