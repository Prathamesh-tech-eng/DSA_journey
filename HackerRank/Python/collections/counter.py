'''Problem Description : I am a shop owner. And I have a list of shoe-sizes. and I am provided a customers desired shoe - size, and the
                         price they are paying for that. Now I need to find the total money I earn from selling
                         e.g : A = [6,6,8]  C1 = 6 45  C2 = 7 70   C3 = 6 35   O/P : 45 + 70 + 35 = 150
                         Link : https://www.hackerrank.com/challenges/collections-counter/problem
                         
                         
Approach : I will first create a dictionary about availability of shoes using Collections.Counter(), and then for each size demand i will
           also update the dictionary and reduce the specific shoe quantity, and I will also store the price simultaneosly. In the end I 
           will print the total price
'''
import collections
A_size = int(input())
A = list(map(int, input().split()))
n = int(input())
total = 0
A = collections.Counter(A)
for i in range(n):
    customer = list(map(int, input().split()))
    if A[customer[0]] >= 1:
       A[customer[0]] -= 1
       total += customer[1]
    
print(total)

#Time complexity : O(m + n)  where m = A_size   n = no. of customers  and A = collections.Counter(A) → O(m)
#Space Complexity : O(m)