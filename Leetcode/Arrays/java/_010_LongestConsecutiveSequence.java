package Leetcode.Arrays.java;
/*
Problem Description : We are provided with unsorted array consisting of integers. Our task is to find the longest consecutive subsequence in O(n) Time
                      Complexity Strictly.
                      e.g : [1,23,11,2,34,3,4,5]  O/P : 5

Problem Approach : By iterating over using for loop and maintaining varaiable LCS (Longest Consecutive Subsequence) and Crr(Current) we can find the longest
                   subsequence in O(n3) time complexity. We can further improve complexity by sorting the provided array before hand and then 
                   while traversing, checking if difference of present and next element is 1 to confirm subsequence, if it is 0 (which indicates
                   a duplicate), we will ignore it and just move to next index, and we will update LCS and crr accordingly, if the difference 
                   result is neither, we will just reset the parameters, and move to next index. This will cost us O(nlogn) time complexity. We 
                   can further optimize it by using hashset, and maintaing the variables LCS and crr. The logic here will to finding the start of
                   the subsequece, if we do find, we can get total the length of the subsequence.we will find subsequence length only after finding
                   the starting element of the subsequence. So we will find if prev element exits for the current element, if yes we will just continue,
                   once we across an element whose prev element is not present then we will use while loop to find the total subsequence length. 
                   Then in the end we will return the maximum subsequence length

#Link : https://leetcode.com/problems/longest-consecutive-sequence/description/
*/

//import java.util.Arrays;
import java.util.HashSet;

//Brute Force Approach 
/*
public class _010_LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums){

        if(nums == null || nums.length==0){
            return 0;
        }

        int maxLCS = 0;

        //Step 1 : Iterate through every number in the array
        for(int i = 0; i < nums.length; i++){
            int currentNum = nums[i];
            int currentStreak = i;

            //Step 2 : Checking if further Subsequence exists
            while (arrayContains(nums, currentNum + 1)){
                currentNum += 1;
                currentStreak += 1;
            }

            maxLCS = Math.max(maxLCS, currentStreak);
        }
        return maxLCS;
    }

    private boolean arrayContains(int[] nums, int target){
        for (int num : nums){
            if(num == target){
                return true;
            }
        }
        return false;
    }
}

    //Time Complexity : O(n3)
    //Space Complexity : O(1)

*/



//Better Approach - Sorted array 
/*
public class _010_LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums){

        if(nums == null || nums.length==0){
            return 0;
        }

        //sort the array (O(NLogN))
        Arrays.sort(nums);
        int longestStreak = 1;
        int currentStreak = 1; 

        //Step 2 : Iterate and count
        for(int i = 1; i < nums.length; i++){
            if(nums[i] == nums[i-1]){
                continue;

            }
            if(nums[i] - nums[i-1] == 1){
                currentStreak += 1
            }

            else{
                longestStreak = max(longestStreak, currentStreak)
                currentStreak = 1
            }
        return max(currentStreak, longestStreak)
        }

    }
}

    //Time Complexity : O(nlogn)
    //Space Complexity : O(n)

*/

public class _010_LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums){

        if(nums.length == 0){
            return 0;
        }
        
        //Step 1 : Creating HashSet
        HashSet<Integer> numSet = new HashSet<>();

        //Step 2 : adding elements in Hashset (duplicates will be removed by default)
        for(int i = 0; i < nums.length; i++){
            numSet.add(nums[i]);
        }

        int longestSub = 1;

        for(int num: numSet){
            if(numSet.contains(num - 1)){
                continue;
            }
            else{
                int currentNum = num;
                int currentSub = 1;
                while (numSet.contains(currentNum + 1)){
                    currentNum++;
                    currentSub++;
                }

                longestSub = Math.max(currentSub, longestSub);
            }
        }
        return longestSub;
    }
}

//Time Complexity : O(n)
//Space Complexity : O(1)