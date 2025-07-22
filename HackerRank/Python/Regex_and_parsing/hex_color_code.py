'''Problem Description : I am provided n lines of css codes, containing hex color codes, my task is to print the valid hex color codes
                         seperately. A valid hex_color_code follows the below conditions :
                         a. it must start with #
                         b. can have 3 or 6 digits
                         c. each digit is in range of 0 to F i.e [0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]
                            where A-F letter can also be lowercase.
                        
                        valid : #EEE  #123  #A1B2CF    Invalids : #defa   #eeeabc
                        Link : https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true
                        
Approach : I will use re (regular expression) for identifying valid hex color codes. I will Extract everything inside { ... } using re.findall
           and and combine using join, then match the valid hex code
           '''
import re

n = int(input())
lines = [input() for _ in range(n)]
css = "\n".join(lines)


blocks = re.findall(r'\{[^}]*\}', css)


block_text = ' '.join(blocks)


pattern = r'#[a-fA-F0-9]{3}(?![a-fA-F0-9])|#[a-fA-F0-9]{6}(?![a-fA-F0-9])'

matches = re.findall(pattern, block_text)

for match in matches:
    print(match)

#Tima Complexity : O(n + T + B) ≈ O(T) where B is total characters inside all {...} blocks and  T is the total number of characters in all lines
#Space Complexity : O(T + B + H) ≈ O(T)