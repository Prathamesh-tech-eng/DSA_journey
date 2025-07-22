'''Problem Description : I am provided a string and I need to check if it is a valid roman number , if yes return true, else false
                         e.g : VI  O/P : True
                         Link : http://hackerrank.com/challenges/validate-a-roman-number
                         
Approach : I will use the characters used in roman numerical i.e : MDCLXVI , and will apply it in regular expression of python
'''

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	

import re
print(str(bool(re.match(regex_pattern, input()))))

#Time Complexity : O(n)
#Space Complexity : O(n)