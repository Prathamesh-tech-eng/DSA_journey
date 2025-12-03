'''
Problem Description : I am provided with an array and an target number. My 
                      goal is to find the numbers with the array such that they
                      sum up to the given target number.

                      e.g [2,3,4,5,6] target : 9    ans : [4,5],[3,6]




Approach : I am planning to use hash map to store the compliment of the numbers while 
           iterating through the array, wheneve a number requires a compliment, it will
           be checked in hash map, if it is present is returned else it iterates till the 
           end, if none is found that sums up to the target, we just return empty array
'''


#Brute force : Linear Search 
'''
def twoSum(nums, target) :
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target :
                return [i,j]
'''


#Sort + Binary Search Approach
'''
import bisect

def twoSum(nums, target) :
    arr = [(nums, i) for i, num in enumerate(nums)]
    arr.sort()         #TimSort

    for i in range(len(arr)):            #Binary search
        complement = target - arr[i][0]
        j = bisect.bisect_left(arr, (complement, 0))

        if j < len(arr) and arr[j][0] == complement and j != 1:
            return [arr[i][1], arr[j][1]]

Time Complexity : O(nlogn)
Space Complexity : O(1)
'''


def twoSum(nums, target):
    seen = {} #value -> index
    
    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i

    return []


'''
    Python's dictionary works like hashmap, so we don't need to import anything
    Time Complexity : O(n)
    Space Complexity : O(n)
'''