'''Problem Description : I am provided a string, and i need to find the first alphanumeric character that has consecutive repetitions
                         e.g : s = 109875.43.123     O/P : 1
                         Link : https://www.hackerrank.com/challenges/re-group-groups
                         
Approach : I will use the re (regular expression) in python, I will use \w or [a-zA-Z0-9] to only consider the alphanumeric character
           and will use \1 to store the first repetition , and use group to print it
'''
import re
s = input()
match = re.search(r"([a-zA-Z0-9])\1",s)

if match : 
    print(match.group(1))
else :
    print(-1)

#Time Complexity : O(n)
#Space Complexity : O(1)