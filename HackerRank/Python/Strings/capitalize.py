'''Problem Description : I am provied a string contianing a person's first name and last name, and I am supposed to 
                         print the first name and last name with there first characters capitialized
                         e.g : prathamesh chikkali  O/P : Prathamesh Chikklai
                         Link : https://www.hackerrank.com/challenges/capitalize
                
Approach : I will split the string, and capitalize first character each one seperately using capitalize(), and the use join() to join them
'''
def solve(word):
    lst = word.strip().split()            #O(n) + O(n)
    lst2 = []
    for i in lst:
        lst2.append(i.capitalize())       #O(n)
    lst2 = " ".join(lst2)                 #O(n)
    print(lst2)

s = input()
print(solve(s))

#Time Complexity : O(4n) i.e O(n)
#Space Complexity : O(n)