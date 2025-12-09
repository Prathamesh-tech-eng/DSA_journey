'''
Problem Description : We are Provided with an unsorted array of integers and our task is to find the missing positive number strictly in O(n) time 
                      complexity and O(1) space Complexity
                      e.g : [-2,34-4,3,1]  O/p : 2

Problem Approach : We can Iterate over to check if the sequence 1,2,3,... is present, but it will cost us O(n2) time complexity. We can try sorting
                   the array and then checking, but the time complexity would still be O(nlogn). If we observe, we can see that the First missibg 
                   Positive number is between 1 and n+1 range and we do not need the -ve no. so If we use dictionary to store the array, with all -ve
                   number's value as 1 and the positive no. stored with same value, we get O(n) time complexity. But the problem is, we won't be able
                   to achieve the constant space complexity i.e O(1).
                   Optimal Logic : 
                   Step 1 : We will convert all -ve no. to 1
                   Step 2 : we will stop at first no. > 1 , go to that indexed no, and change that no. to -ve, and also to indexed no present there as
                            value, change that no. to -ve and so on.
                   Step 3 : we will start iterating from indx 2 , the first +ve 1 valued index no. is our first missing positive number.
                   
Link : https://leetcode.com/problems/first-missing-positive/
'''

#Brute Force :
'''
def firstMissingPositive(nums):
    ans = 1
    while True:
        if ans not in nums:
            return ans
        ans += 1
'''

#Time Complexity : O(n2)
#Space Complexity : O(1)

#Sorted Array : 
'''
def firstMissingPositive(nums):
    nums.sort()
    target = 1
    for n in nums:
        #if we found the target we are looking for we need the next one
        if n == target:
            target += 1

        #if the current number is greater than our target, we found the gap
        elif n > target:
            return target
            
    #If we finish the loop the missing number is the next one
    return target
'''

#Time Complexity : O(nlogn)
#Space Complexity : O(1)

#Set Approach : 
'''
def firstMissingPositive(nums):
    num_set = set(nums)
    ans = 1
    while True:
        if ans not in num_set:
            return ans
        ans += 1
        '''

#Time Complexity : O(n)
#Space Complexity : O(n)



#Cyclic Sort Approach : 
def firstMissingPositive(nums):
    n = len(nums)
    i = 0

    #Cyclic Sort : Place numbers in correct spots
    while i < n:
        correct_index = nums[i] - 1

        if 0 < nums[i] < n and nums[i] != nums[correct_index]:
            nums[i] , nums[correct_index] = nums[correct_index] , nums[i]
        else:
            i += 1

    # Scan to find the first mismatch
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
        
    # If all positions are correct, the missing number is n + 1
    return n + 1

#Time Complexity : O(n)
#Time Complexity : O(1)