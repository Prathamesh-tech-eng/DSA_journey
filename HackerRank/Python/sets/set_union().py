'''Problem Description : I am given two lists, one who are subscribed to english newspaper and the other one who are subscribed to 
                         french newspaper. my job is to print the total no. of students who are subscribed to atleast one newspaper
                         link : https://www.hackerrank.com/challenges/py-set-union
                         
Approach : I will use convert them to sets and use union(), and then print the final length of set
'''

A_size = int(input())
A = set(map(int, input().split()))    #O(n)
B_size = int(input())
B = set(map(int, input().split()))    #O(m)

C = A.union(B)                        #O(n + m)
print(len(C))


#Time complexity : O(n + m)
#Space Complexity : O(n + m)