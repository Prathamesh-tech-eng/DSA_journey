'''Problem Description : I am provided with a string and I am suppsed to tell wheter it contains character that is alphanumric  (a-z, A-Z and 0-9),
                         alphabetic  (a-z and A-Z), digit (0-9), lowercase (a-z), uppercase (A-Z).
                          e.g : Prat23  O/P : True True True True True
                         Link : https://www.hackerrank.com/challenges/string-validators 
                         
Approach : python provides built in functions for this : isalnum(), isalpha(), isdigit(), isupper(), islower()'''

s = input()
    
print(any(c.isalpha() for c in s))    #O(n)       i.e any() while the other prebuilt functions only has O(1)
print(any(c.isdigit() for c in s))    #O(n)
print(any(c.isalnum() for c in s))    #O(n)       
print(any(c.islower() for c in s))    #O(n)
print(any(c.isupper() for c in s))    #O(n)


#Time Complexity: O(5n) that is O(n)

