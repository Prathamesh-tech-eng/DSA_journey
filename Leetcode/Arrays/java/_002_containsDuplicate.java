package Leetcode.Arrays.java;
// import java.util.Arrays;
import java.util.HashSet;
/*
Probliem Description : I am Provided with an array, and i just need to check if duplicates
                        are present in the array, and return true if there are.
                        e.g [11,22,22,33,44]       O/P : True

Problem Approach : I can use linear search(brute force) or sort + Linear Search . But the most
                    most optimal apprach is using an other data structure to store and check for 
                    duplicates. In this case using hash will be most optimal , we can access elements
                    in O(1)
*/

public class _002_containsDuplicate {
   public boolean solution(int[] nums){
// Brute force Approach :
/*
        for( int i = 0; i < nums.length; i++){
            int target = nums[i];
            for(int j = 0; j < nums.length; j++){
                if( nums[j] == target){
                    return true;
                }
            }
        }
        return false;

        Time Complexity : O(n2)
        Space Complexity : O(n)
*/

// Sorting + Linear Search 
/*
    Arrays.sort(nums);
    for( int i = 1; i < nums.length; i++){
            int target = nums[i];
            if( nums[i-1] == target){
                    return true;
            }
        }
        return false;

        Time Complexity : O(nlogn)
        Space Complexity : O(nlogn)
*/

// Using Hashset
    HashSet<Integer> seenNumbers = new HashSet<>();

    for(int num : nums){
        if(seenNumbers.contains(num)){
            return true; //Duplicate found
        }
        seenNumbers.add(num);
    }
    return false;
    }
}
