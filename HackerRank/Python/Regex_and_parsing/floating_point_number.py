'''Problem Description : I am provided with a number I need to check if it satisfies the following conditions:
                            Number can start with +, - or . symbol.
                            For example: +4.50, -1.0, .5, -.7, +.4, -+4.5
                            Number must contain at least  decimal value.
                            For example: 12. ,12.0 
                            Number must have exactly one . symbol.
                            Number must not give any exceptions when converted using .
                            
                            Link : https://www.hackerrank.com/challenges/introduction-to-regex
                            
Approach : I will use re (regular expression) to check for the conditions and print the result
'''

import re

isdecimal = lambda s: bool(re.match(r"^[+-]?(\d*\.\d+)$", s))

n = int(input())
for _ in range(n):
    x = input()
    print(isdecimal(x))


#Time Complexity : O(n * L)  where L is len(x)
#Space Complexity : O(1)