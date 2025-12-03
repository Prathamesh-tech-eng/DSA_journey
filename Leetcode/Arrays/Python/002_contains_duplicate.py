'''
Probliem Description : I am Provided with an array, and i just need to check if duplicates
                        are present in the array, and return true if there are.
                        e.g [11,22,22,33,44]       O/P : True

Problem Approach : I can use linear search(brute force) or sort + Linear Search . But the most
                    most optimal apprach is using an other data structure to store and check for 
                    duplicates. In this case using hash will be most optimal , we can access elements
                    in O(1)
'''

#Brute Force Apprach
'''
def contain_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] : return True
        
        return False

Time Complexity : O(N2)
Space Complexity : O(1)
'''

#Sorting + Linear Seach Approach 
'''
def contain_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] : return True
    
    return False

Time complexity : O(nlogn)
Space Complexity : O(1)
'''

#using Hashset
def contain_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen : return True
        seen.add(num)
    return False

## Second Approach 
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

'''
Time Complexity : O(n)
Space Complexity : O(n)
'''