'''
Problem Description : I am provided with an array and an number k, and i need to find duplicates such that absolute difference of these duplicates
                      would end up less than the integer k.
                      e.g : [2,3,4,5,4]    k = 2     O/P : abs(2-4) = 2 <= 2 so it satisfies the condition and we return True.

Problem Approach : for Brute force we could just iterate each time till next k values, and check for duplicates, to improve more we can sort and then
                   check for duplicates in the next k values. To optimize further, we can use a different datastructure i.e dictionary to store key (index) ->
                   value pairs, and will check for duplicates in k values. i.e Sliding window + dictionary
'''
#Brute Force Approach : 
'''
def contain_Duplicate2(nums, k) :
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and math.abs(i - j )<ds= k : return True
    return False


Time Complexity : O(n*k)
Space Complexity : O(1)
'''

#Sort + Sliding Window Approach 
'''
def contain_Duplicate2(nums, k):
    arr = [(nums,i) for i, nums in enumerate(nums) ]
    arr.sort()

    for i in range(1, len(nums)):
        if arr[i][0] == arr[i-1][0] and abs(arr[i][1] - arr[i-1][1]) <= k :
            return True
    return False
    

Time Complexity : O(nlogn)
Space Complexity : O(n)
'''


#best approach
def containsNearbyDuplicate(nums, k):
    seen = {}

    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        
        seen[num] = i  #update to latest index

    return False

'''
Time Complexity : O(n)
Space Complexity : O(n)
'''