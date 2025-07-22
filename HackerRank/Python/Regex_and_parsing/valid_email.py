'''Problem Description : I am provided a lot of mails and i need to identify the valid once and only return them.
                         the condition for valid mails are :
                         a. A mail is in format username@domain.extension
                         b. A username starts with aphabet and can consist of alphanumric characters, -, . or _
                         c. A domain always consists of only alphabets
                         d. A extension consists of 1,or atmax 3 characters
                         
                         e.g : ABC <ABC@gmail.com>
                               XYZ <XYZ!!@gmail.com>
                               O/p : ABC <ABC@gmail.com>
                               
                        Link : https://www.hackerrank.com/challenges/validating-named-email-addresses
                        
Approach : I will use email.utils.parseaddr for obtaining seperate username and email, and then I will apply the conditions using re
           (regular expresion), and in the end I will print the valid mail using email.utils.formataddr
           
'''

import re
import email.utils

n = int(input())

for i in range(n):
    user_mail = email.utils.parseaddr(input())
    mail = user_mail[1]
    valid_mail = r"^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
    if re.match(valid_mail, mail):
        print(email.utils.formataddr(user_mail))

#Time Complexity : O(n)
#Space Complexity : O(n * L)  where L : length of input mail