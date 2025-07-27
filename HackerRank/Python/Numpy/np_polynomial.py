'''Problem Description : I am provided a Polynomial coefficient , I need to print the value of polynomial at given x value.
                         e.g : 1, 2   x = 3  O/p : 5
                         Link : https://www.hackerrank.com/challenges/np-polynomials
                         
Approach : I will use np.polyval() to evaluate the polynomial at the given x value.
'''
import numpy as np

coeffs = np.array(list(map(float, input().split())))
x = int(input())

print(np.polyval(coeffs, x))

#Time Complexity : O(N)
#Space Complexity : O(N)