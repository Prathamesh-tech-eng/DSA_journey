package Leetcode.Arrays.java;

//import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/*
Problem Description : I am provided with an array and an number k, and i need to find duplicates such that absolute difference of these duplicates
                      would end up less than the integer k.
                      e.g : [2,3,4,5,4]    k = 2     O/P : abs(2-4) = 2 <= 2 so it satisfies the condition and we return True.

Problem Approach : for Brute force we could just iterate each time till next k values, and check for duplicates, to improve more we can sort and then
                   check for duplicates in the next k values. To optimize further, we can use a different datastructure i.e hashmap to store key (index) ->
                   value pairs, and will check for duplicates in k values. i.e Sliding window + (hashmap or hashset)
*/

public class _003_containsDuplicate2 {
    public boolean containNearbyDuplicate(int[] nums, int k){



        //Brute Force : 
        /*
        for(int i = 0; i < nums.length; ++i){
            for(int j = 1; j < k; ++j){
                if(nums[i] == nums[j] && Maths.abs(i - j) <= k) return true;
            }
        }
        return false;

        Time Complexity : O(n*k);
        Space Complexity : O(1);

        */



        //Sort + Sliding Window
        /*
        n = nums.length();
        
        int[][] arr = new [n][2];   //[value, orignalIndex]
        for(int i = 0; i < n; i++){
        arr[i][0] = nums[i];  // Value
        arr[i][1] = i;        // Orignal Index
        }

        //Sort by value then by index
        Arrays.sort(arr, (a,b) ->  {
            if (a[0] != b[0]){
                return Integer.compare(a[0], b[0]); //Compare values
            }
                return Integer.compare(a[1], b[1]); //Compare indices if same value
        });

        for (int i = 1; i < n; i++) {
            if (arr[i][0] == arr[i - 1][0] &&
                Math.abs(arr[i][1] - arr[i - 1][1]) <= k) {
                return true;
            }
        }

        return false;
        
        }
        
        Time Complexity : O(nlogn);
        Space Complexity : O(n);

        */




        // HashSet + Sliding window

        Set<Integer> set = new HashSet<>();
        for(int i = 0 ; i < nums.length; ++i){
            if(set.contains(nums[i])) return true;
            set.add(nums[i]);
            if(set.size() > k){
                set.remove(nums[i - k]);
            }
        }
        return false;

        
        // Time Complexity : O(n);
        // Space Complexity : O(n);
    }
}
