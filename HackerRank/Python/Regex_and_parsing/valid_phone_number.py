'''Problem Description : I am Provided a string , I need to check if it is a valid phone number.
                         e.g : 7972080461   O/P : Yes
                         Link : http://hackerrank.com/challenges/validating-the-phone-number
                         
Approach : I will use re from built in, a valid phone no. is 10 digit and typically starts from 7,8 or 9, I will add this condition and
           print the result
           
           '''
import re
n = int(input())
for i in range(n):
    x = input()
    mobile_no = r"^[789]\d{9}$"
    if re.match(mobile_no, x):
        print("YES")
    else :
        print("NO")

#Time Complexity : O(n)
#Space complexity : O(1)
