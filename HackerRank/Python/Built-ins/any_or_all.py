'''Problem Statement : I am provided with list, and I am supposed to check if all the elements in the list are positive and if they are
                       any palindromic integer, and if there are I need to print true, else false
                       e.g : [1, 2, 3]    O/P : True
                       Link : https://www.hackerrank.com/challenges/any-or-all
                       
Approach : I will use all() to find whether all elements in the given list are positive or not, and further to check for palindromic
           integer I will use any(), the condition will be str(i) == str(i)[::-1]
           '''

A_size = int(input())
A = list(input().split())
if all(int(i) > 0 for i in A ):
    print(any(A[i] == A[i][::-1] for i in range(A_size)))
else : 
    print("False")


#Time Complexity : O(n * A_size):
#Space Complexity : O(A_size)