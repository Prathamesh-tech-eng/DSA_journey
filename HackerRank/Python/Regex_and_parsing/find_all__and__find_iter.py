'''Problem Description : I am Provided with string containing alphanumeric characters, spaces, +, _ and my task is to find all the substrings that
                         lie between two consonants and must only consist of vowels
                         e.g : Prathamesh   O/P : a, e
                         link : https://www.hackerrank.com/challenges/re-findall-re-finditer
                         
                         
Approach : I will use regular expression to check for the vowels and consonants and return the substrings
'''

import re
s = input()

pattern = r'(?i)(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])'

matches = re.findall(pattern, s)

if matches:
    for m in matches :
        print(m)
else :
    print(-1)

#Time Complexity : O(n)
#Space Complexity : O(n)