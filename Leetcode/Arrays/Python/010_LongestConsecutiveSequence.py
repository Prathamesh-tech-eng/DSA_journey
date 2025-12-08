'''
Problem Description : We are provided with unsorted array consisting of integers. Our task is to find the longest consecutive subsequence in O(n) Time
                      Complexity Strictly.
                      e.g : [1,23,11,2,34,3,4,5]  O/P : 5
                      
Problem Approach : By iterating over using for loop and maintaining varaiable LCS (Longest Consecutive Subsequence) and Crr(Current) we can find the longest
                   subsequence in O(n3) time complexity. We can further improve complexity by sorting the provided array before hand and then 
                   while traversing, checking if difference of present and next element is 1 to confirm subsequence, if it is 0 (which indicates
                   a duplicate), we will ignore it and just move to next index, and we will update LCS and crr accordingly, if the difference 
                   result is neither, we will just reset the parameters, and move to next index. This will cost us O(nlogn) time complexity. We 
                   can further optimize it by using set, Convert the input array into set, which will eliminate all the duplicates
                    1. Iterate through each number in set num
                    2. check if num - 1 exits for the element, it exits skip and go to next element
                    3. if it does not exit, enter a while loop and check for num + 1, num + 2 , etc.
                    4. Update the global maxLength with this sequence's count and return the maximum after checking all numbers.

#Link : https://leetcode.com/problems/longest-consecutive-sequence/description/
'''

#Brute Force Approach
'''
def longestConsecutive(nums):

    if nums == None or len(nums) == 0 :
        return 0
    
    maxLCS = 0

    #Step 1 : Iterate through every element in the array
    for i in range(len(nums)):
        currentNum = nums[i]
        currentStreak = 0

        #Step 2 : checking if further subsequence exits
        while currentNum in nums:
            currentNum += 1
            currentStreak += 1

        maxLCS = max(maxLCS, currentStreak)

    return maxLCS
'''
#Time Complexity : O(n3)
#Space Complexity : O(n)

#Sorted Approach
'''
def longestConsecutive(nums):

    if nums == None or len(nums) == 0:
        return 0
    
    nums = sorted(nums)
    longestStreak, currentStreak = 1, 1

    #Iterating and counting the sorted array
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            currentStreak += 1

        elif nums[i] == nums[i-1]:
            continue

        else :
            longestStreak = max(longestStreak, currentStreak)
            currentStreak = 1

    return max(longestStreak, currentStreak)

'''
#Time Complexity : O(n3)
#Space Complexity : O(n)

#Set approach
def longestConsecutive(nums):

    if nums == None or len(nums) == 0:
        return 0
    
    num_set = set(nums)
    longestSub = 0

    for num in num_set : 
        if (num - 1) not in num_set:
            currentNum, currentSub = num, 1

            while (currentNum + 1) in num_set :
                currentNum += 1
                currentSub += 1
            longestSub = max(currentSub, longestSub)

    return longestSub

#Time Complexity : O(n)
#Space Complexity : O(n)