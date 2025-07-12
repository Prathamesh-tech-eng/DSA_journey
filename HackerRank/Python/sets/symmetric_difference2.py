'''Problem Description : I am given two lists, one who are subscribed to english newspaper and the other one who are subscribed to 
                         french newspaper. my job is to print the total no. of students who have subscriptions to English or French
                         newspapers but not both
                         e.g A = [11,12,13,14,15]  B = [2,3,14,35,23]  A^B = {2,3,11,12,13,15,23,35}
                         
                         link : https://www.hackerrank.com/challenges/py-set-difference-operation
                         
Approach : I will convert them to sets and use difference(), and then print the final length of set
'''

A_size = int(input())
A = set(map(int, input().split()))    #O(n)
B_size = int(input())
B = set(map(int, input().split()))    #O(n)

C = A.symmetric_difference(B)                   #O(n + m)
print(len(C))

#Time Complexity : O(n + m)
#Space Complexity : O(n + m)
