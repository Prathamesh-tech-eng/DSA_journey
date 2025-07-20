'''Problem Description : I am provided with a single variable polynomial function , and also number x and z, I need to check whether
                         P(x) = z or not.
                         e.g : P(x) = x**2  + 1      I/P :  1 2        O/P : P(1) = 2     so True
                         Link : https://www.hackerrank.com/challenges/input
                           
Approach : I will use Python 2, and directly use input() as it is equivalent to eval(raw_input())
 '''

x , z = map(int, input().split())
expr = input()
print(eval(expr) == z)

#Time Complexity  : O(1)
#Space Complexity : O(1)