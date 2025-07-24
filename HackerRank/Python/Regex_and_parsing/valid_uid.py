'''Problem Description : I am provided many unique id's I need to check whether they are valid or invalid. They mush follow the following 
                         conditions :
                         a. must contain atleast 2 uppercase englisgh alphabet
                         b. must contain atleast 3 digits
                         c. must only contain alphanumeric characters
                         d. no repetition allowed
                         e. there must be total 10 characters
                         
                         e.g : AB123098Cd   O/P : Valid
                         Link : https://www.hackerrank.com/challenges/validating-uid
                         
Approach : I will use re, and re.match to find all the matching patterns
'''
import re
n = int(input())

for i in range(n):
    s = input()
    uid_re = r''