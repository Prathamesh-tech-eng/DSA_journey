'''Problem Description : i am given a list of height of plants, i need to find avg height using the formula avg = sum of distinct 
                         height/total distinct height. e.g : [10, 10, 20, 30, 40]  O/P : 25.000
                         Link : https://www.hackerrank.com/challenges/py-introduction-to-sets

                         
Approach : first convert the list to set and then back to list to get distinct values and use sum() to get sum and len() to 
           get total no. of distinct heights
           '''

def average(array):
    lst = list(set(array))             #O(n) + O(n)
    n = len(lst)
    avg = sum(lst)/n
    return f"{avg:.3f}"


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)

#Time Complexity : O(n)
#Space Complexity : O(n)