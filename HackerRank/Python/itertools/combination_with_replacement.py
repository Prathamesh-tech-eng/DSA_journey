'''Problem Description : I am provided a string and an integer n, i need to print all possible replacement combinations of size n
                         e.g  TALK 2  O/p : TA TL TK AL AK LK
                         Link : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
                         
Approach : I will use the built in function itertools.combination_with_replacement method  with given size and print the result
'''
import itertools
A, n = input().split()
A = sorted(A)                                                               #O(mlogm)  where m = len(A)
for i in itertools.combinations_with_replacement(A,int(n)):
    print("".join(i))


#Time Complexity :  O(C × r)  where : r = int(n) and C = Total combinations
#Space Complexity : O(m + r)
