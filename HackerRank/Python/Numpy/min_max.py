'''Problem Description : I am provided with an array I need to find the smallest numbers along all columns and then among the obtained 
                         values , I need to print the largest number.
                         e.g : [[22 45]
                                [50 3]]     O/P : [22 3] -->  [22]
                         Link : https://www.hackerrank.com/challenges/np-min-and-max
                         
Approach : I will use np.min to find all minimum along axis = 1 and then I will use np.max to find max along axis = 0'''

import numpy as np

N , M = map(int, input().split())

A = np.array([list(map(int, input().split())) for _ in range(N)])
row_min = np.min(A, axis = 1)
print(np.max(row_min, axis = 0))

#Time Complexity : O(N * M)
#Space Complexity : O(N * M)