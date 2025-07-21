'''Problem Description : I am provided a number seperated by "," and "." I need to split the number at these symbols and write the 
                         preceeding digits on next line
                         e.g : 100,000.0    O/P : 100
                                                  000
                                                  0
                         Link : https://www.hackerrank.com/challenges/re-split
                         

Approach : I will use the regular expression in python to identify the symbol and to split them , I will use re.split()
'''

import re
regex_pattern = r",."
print("\n".join(re.split(regex_pattern, input())))

#Time Complexity : O(L)  where L is length of string
#Space Complexity : O(L + P) where P is no. of parts


