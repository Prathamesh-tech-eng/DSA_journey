#Problem Description : I am provided a list of scores and I am supposed to find the second best score from the list
#eg. I/p : [100,20,39,45,200,210,34]   o/p : 200
#link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

#Approach 1: I am planning to delete the duplicates first by converting it into set, and then into list,
#  and then applying sort function.


n = int(input())
arr = map(int, input().split())
    
unique_score = list(set(arr))        #O(n)
unique_score.sort()                  #O(nlogn)

print(unique_score[-2])              #O(1)

#Time Complexity : O(nlogn)

#Approach 2: But I am thinking of an more optimized approach, if i use a single for loop and two variable to keep track of larger and 
# largest number
arr = list(map(int, input().split()))
first = second = -float('inf') 

for score in arr:                    #O(n)
    if score > first:
        second = first 
        first = score    
    elif first > score > second:
        second = score   

print(second)

#Time complexity : O(n)
