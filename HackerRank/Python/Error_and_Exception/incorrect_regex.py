'''Problem Description : I am provided a string, and I need to find whether the given string is a valid regex or not.
                         e.g : abc@xyz.com  O/p : True
                               (\d+         O/p : False
                         Link : https://www.hackerrank.com/challenges/incorrect-regex
        
Approach : I will use the re.compile method of python in try except block , and return true or false
'''
import re

T = int(input()) 
invalid_repeats = ['++', '**', '??', '*+', '?', '+?', '??']

for _ in range(T): 
    S = input().strip()

    # Basic invalid pattern check
    is_invalid = any(rep in S for rep in invalid_repeats)

    if is_invalid:
        print("False")
        continue

    try:
        re.compile(S)
        print("True")
    except re.error:
        print("False")

#Time Complexity : O(n)
#Space Complexity : o(1)