'''Problem Description : I am provided with a set, and i need to perform operations like pop, remove and discard on the set.
                         Link : https://www.hackerrank.com/challenges/py-set-discard-remove-pop
                         
Approach : I will take the inputs in for loop, will divide the input into command and args, and then apply if else to identify 
           the command and in the end will print the resultant set
           '''

A_size = int(input())
A = set(map(int, input().split()))          #O(m)
n = int(input())
for i in range(n):                          #O(n)
    instruction = input().split()
    command = instruction[0]
    if len(instruction) > 1 :
         args = int(instruction[1])
    if command == "discard":
        A.discard(args)
    elif command == "remove":
        A.remove(args)
    elif command == "pop":
        A.pop()
   
 
print(sum(A))                               #O(k)

#Time Complexity : O(m + N + k) = O(m + n)
#Space Complexitu : O(m)