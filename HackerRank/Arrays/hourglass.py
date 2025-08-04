'''Problem Description : I am provided with 6 x 6 matrix, and there are 16 possible hourglass sum , I need to find the one that is maximum
                         Link : https://www.hackerrank.com/challenges/2d-array
                         
Approach : I will use for loops and using basic string slicing to get all the hourglass sum, and the find the one that is maximum
'''

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

lst = []
for i in range(4):
    for j in range(4):
        hourglass = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
        lst.append(hourglass)
lst.sort()
print(lst[-1])

#Time Complexity : O(1)
#Space Complexity : O(1)

#I can avoid sorting by just storing max value at each point.

lst = []
max_sum = -float('inf')
for i in range(4):
    for j in range(4):
        hourglass = (arr[i][j] + arr[i][j+2] + arr[i][j+2]
                             + arr[i+1][j+1] + 
                    arr[i][j] + arr[i][j+2] + arr[i][j+2])
        max_sum = max(max_sum, hourglass)
print(max_sum)

#Time Complexity : O(1)
#Space Complexity : O(1) (reduced)