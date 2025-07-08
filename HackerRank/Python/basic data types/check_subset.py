'''Problem Discription : I am provide two sets and I am supposed to print true if A is subset of B else false
                         eg. A  = {1,2,3,4}  B = {3,4}  O/P : False
                         link : https://www.hackerrank.com/challenges/py-check-subset
                         
Approach : I will apply for loop for A and check if every element Of A is whether present in B or not'''

n = int(input())

for _ in range(n):
    A = input().split(" ")
    B = input().split(" ")

    is_subset = True

    for item in A:
        if item not in B:
            is_subset = False
            break

    print(is_subset) 

#Time complexity : O(m * n)

#Approach 2 : using built in function issubset()
n = int(input())

for _ in range(n):
    A = input().split(" ")
    B = input().split(" ")
    if set(A).issubset(set(B)):
        print("True")
    else:
        print("False")

#Time complexity : O(m + n)

#Approach 3 : can also use the all() function 
for _ in range(n):
    A = input().split()
    B = set(input().split())

    is_subset = all(item in B for item in A)
    print(is_subset)

#time complexity : O(m + n)



