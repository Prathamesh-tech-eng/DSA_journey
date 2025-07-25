'''Problem Description : I am provided an 2D array of dimensions N*M, I need to calculate sum at axis = 0 and the print the product of
                         the result.
                         e.g : 2 2      O/P : 168  (12 * 14)
                               5 6
                               7 8 
                               
                         Link : https://www.hackerrank.com/challenges/np-sum-and-prod
                         
Approach : I will first apply np.sum() at axis = 0 and then apply np.product() at axis = 0
'''

import numpy as np
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = np.sum(A, axis=0)
print(np.prod(result))

#Time Complexity : O(N*M)
#Space Complexity : O(N*M)