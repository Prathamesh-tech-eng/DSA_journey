'''Problem Description : I am provided two integer arrays and I am supposed to print perform basic operations like ADD, subtract, multiply
                         divide, mod, power and print their result.
                         Link : https://www.hackerrank.com/challenges/np-array-mathematics
                         
Approach : I will first convert the given list into arrays using np.array(), and then I will use operands like +,-,*,/,%,** for printing
           the required operation result
           '''
import numpy as np
N, M = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(N)])
B = np.array([list(map(int, input().split())) for _ in range(N)])

print(f"{A+B}\n{A-B}\n{A*B}\n{np.floor_divide(A, B)}\n{A%B}\n{A**B}")

#Time Complexity : O(N*M)
#Space Complexity : O(N*M)
