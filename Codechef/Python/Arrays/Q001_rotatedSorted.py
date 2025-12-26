'''
Problem description: We are expected to return if the array is sorted at some point if you rotate the array. 
                     A sorted array consists of increasing order. The gist of the problem is the realization that an sorted
                     rotated array will have only one break point.
                     e.g i/p: [5,1,2,3,4] ---> after rotation [1,2,3,4,5] sorted = true so,  o/p : true 

Approach : 
            Now there are two approaches :
            1.Whether you check if the array is sorted .
            2.Whether you find the total break points.
            Approach 1 is lengthy, it was the first approach e did myself, before realizing about the break points. All you do here is find the minimum element of the array, and from that array you check if the array is further sorted. Then you iterate from start to minimum to check if it is sorted, and then some few edge cases.

            Approach 2: we will just count the total break points , and check if they are less than 1. If not, we will return false.
                        e.g : [1,2,3,4,5] ---> break points = 0; [5,1,2,3,4] ----> break Points = 1; (as arr[0] > arr[1]
            

Link : https://www.codechef.com/practice/course/arrays/ARRAYS/problems/ARRAYSORTED?tab=statement
'''





class Solution(object):
    def check(self, nums):
        
        n = len(nums)
        count = 0
    
        for i in range(n-1) :
            if nums[i] > nums[i + 1] : 
                count += 1
            
        
    
        # Check last and first element
        if nums[n - 1] > nums[0] : 
            count+=1
        
    
        return count <= 1
    
# Time Complexity : O(n)
# Space Complexity : O(1)