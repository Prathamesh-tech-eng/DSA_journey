'''Problem Description : I am provided a list and a which is out main set, and other lists as input, I need to check whether the main
                         set is super set of all other provided sets

                         e.g : A : {11,12,13,14}   B : {13, 14}  O/p : True (A is superset of B)
                         Link : https://www.hackerrank.com/challenges/py-check-strict-superset

Approach : I will use the built in function to find whether the given set is a subset or not .issubset(). And in end for all lists the result 
           must be true for it to be superset(), else it is not.
                         '''


A = set(map(int, input().split()))            #O(n)
n = int(input())

result = True
for i in range(n):                            #O(n)
    B = set(map(int, input().split()))        #O(k)
    if B.issubset(A) == False:
        result = False
        
print(result)



#Time complexity : O(m + n*k)
#Space Complexity : O(m + k)

