'''Problem Disciption : I am provided with a string, I need to divide the string into max width provided and print each resulting 
                        string on a new line. e.g : PRATHAMESH  width = 4  O/p : PRAT
                                                                                 HAME
                                                                                 SH
                        link : https://www.hackerrank.com/challenges/text-wrap
                        
Approach : I am planning to create a function which will take the string the max width as parameter, then using textwrap.wrap()
           I can easily create a list of strings with mentioned width, then I will join the list using join(), with new line
           '''

import textwrap
 
def wrap(string, max_width):
    result = textwrap.wrap(string, max_width)
    word = "\n".join(result)
    return word

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

#Time complexity : O(n) 