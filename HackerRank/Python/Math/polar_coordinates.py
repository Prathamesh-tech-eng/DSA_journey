'''Problem Description : I am provided a complex number and I need to find (r, θ) i.e the polar coordinates using the complex number.
                         e.g : 1 + 2j    O/P : r = root(5)  z = arctan( x/y​ )
                         Link : https://www.hackerrank.com/challenges/polar-coordinates
                         
Approach : I will use the built in function in python i.e : cmath'''

import cmath
A = complex(input()) 
r, radian = cmath.polar(A)

print(f"{r:.3f}\n{radian:.3f}")

#Time Complexity : O(1)
#Space Complexity : O(1)