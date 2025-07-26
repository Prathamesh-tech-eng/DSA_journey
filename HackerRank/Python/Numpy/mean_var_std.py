'''Problem Description : I am provided an array I need to calculate mean of it's rows, then variance of the obtained values, and in the 
                         end print the standard deviation of the result.
                         link : https://www.hackerrank.com/challenges/np-mean-var-and-std
                         
Approach : I will use np.mean, np.var and np.std to calcultae mean , standard deviation and variance. I will mention axis = 1 for columns
'''

import numpy as np

N, M = map(int, input().split())

A = np.array([list(map(int, input().split())) for _ in range(N)])
row_mean = np.mean(A, axis = 1)
col_var = np.var(A, axis = 0)
stand_dev = round(np.std(A),11)
print(f"{row_mean}\n{col_var}\n{stand_dev}")


#Time Complexity : O(N * M)
#Space Complexity : O(N * M)