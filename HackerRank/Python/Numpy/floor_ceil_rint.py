'''Problem Description : I am provided an array I need to print their floor, ceil and rint values.
                         Link : https://www.hackerrank.com/challenges/floor-ceil-and-rint

Approach : I will use the numpy built in for finding floor, ceil and rint values, i.e : np.floor, np.ceil and np.rint()
'''
import numpy as np
np.set_printoptions(legacy=1.15)
A = np.array(list(map(float, input().split())))

print(f"{np.floor(A)}\n{np.ceil(A)}\n{np.rint(A)}")


#Time Complexity : O(N)
#Space Complexity : O(N)