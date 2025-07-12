'''Problem Description : I am given two lists, one who are subscribed to english newspaper and the other one who are subscribed to 
                         french newspaper. my job is to print the total no. of students who are subscribed to both newspaper
                         link : http://hackerrank.com/challenges/py-set-intersection-operation
                         
Approach : I will convert them to sets and use intersection(), and then print the final length of set
'''

A_size = int(input())
A = set(map(int, input().split()))    #O(n)
B_size = int(input())
B = set(map(int, input().split()))    #O(n)

C = A.intersection(B)                 #O(n + m)
print(len(C))

#Time Complexity : O(n + m)
#Space Complexity : O(min(n + m))