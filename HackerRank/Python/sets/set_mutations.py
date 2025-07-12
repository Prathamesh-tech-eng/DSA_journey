'''Problem Description : I am provided with a set. I need to perform operations like .update(), .intersection_update(), .difference.update()
                         .symmetric_difference_update(). where along with each operation I am provide an another set, which i need 
                         to use while performing the operation. And I need to print the sum of resultant set elements
                         e.g : A = [11,12,13,14,15]  B = [2,3,14,35,23]  A|B = {2,3,11,12,13,14,15,23,35}
                         Link : https://www.hackerrank.com/challenges/py-set-mutations

Approach : I will take the input then, split the instruction into list, apply if-else to identify the operation, and print the 
           sum of resultant set.'''

A_size = int(input())
A = set(map(int, input().split()))                      #O(a)
n = int(input())

for i in range(n):                                      #O(n)
    instruction = input().split()
    B = set(map(int, input().split()))                  #O(b)
    command = instruction[0]
    size = instruction[1]

    if command == "intersection_update" :               #O(min(a, b))
        A.intersection_update(B)
    elif command == "symmetric_difference_update" :     #O(n + b)
        A.symmetric_difference_update(B)
    elif command == "difference_update":                #O(b)
        A.difference_update(B)
    elif command == "update":                           #O(b)
        A.update(B)

print(sum(A))

#Time Complexity : O(a + nb)
#Space Complexity : O(a + b)