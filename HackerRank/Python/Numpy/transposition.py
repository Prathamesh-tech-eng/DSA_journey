'''Problem Description : I am provided an array as an input in need to print it's transpose and also as a 1D list.
                         e.g : [[1 3]
                                [5 7]]       O/P  [[1 5]      [1 3 5 7]
                                                   [3 7]]     
                                                   
                        Link : https://www.hackerrank.com/challenges/np-transpose-and-flatten
                        
Approach : I will use the built in np.traspose and np.flatten to print the transpose and 1D list.
'''
import numpy as np
N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
A = np.array(A)

print(np.transpose(A))
print(A.flatten())

#Time Complexity : O(N * M)
#Space Complexity : O(N * M)

