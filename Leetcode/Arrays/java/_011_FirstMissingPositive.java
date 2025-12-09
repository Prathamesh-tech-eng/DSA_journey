package Leetcode.Arrays.java;

/*
Problem Description : We are Provided with an unsorted array of integers and our task is to find the missing positive number strictly in O(n) time 
                      complexity and O(1) space Complexity
                      e.g : [-2,34-4,3,1]  O/p : 2

Problem Approach : We can Iterate over to check if the sequence 1,2,3,... is present, but it will cost us O(n2) time complexity. We can try sorting
                   the array and then checking, but the time complexity would still be O(nlogn). If we observe, we can see that the First missibg 
                   Positive number is between 1 and n+1 range and we do not need the -ve no. so If we use HashMap to store the array, with all -ve
                   number's value as 1 and the positive no. stored with same value, we get O(n) time complexity. But the problem is, we won't be able
                   to achieve the constant space complexity i.e O(1).
                   Optimal Logic : 
                   Step 1 : We will convert all -ve no. to 1
                   Step 2 : we will stop at first no. > 1 , go to that indexed no, and change that no. to -ve, and also to indexed no present there as
                            value, change that no. to -ve and so on.
                   Step 3 : we will start iterating from indx 2 , the first +ve 1 valued index no. is our first missing positive number.
                   
Link : https://leetcode.com/problems/first-missing-positive/
*/


//Brute Force : 
/*
public class _011_FirstMissingPositive {
    public int firstMissingPositive(int[] nums){

        int ans = 1;
        while(true){
            boolean found = false;

            for(int j = 0; j < nums.length; j++){
                if(nums[j] == ans){
                    found = true;
                    break;
                }
            }
            
            if(!found){
                return ans;
            }

            ans++;
        }
        return ans;
    }
}

*/

//Time Complexity : O(n2)
//Space Complexit : O(1)

//Sorted Array Approach 
/*
public class _011_FirstMissingPositive {
    public int firstMissingPositive(int[] nums){
        Arrays.sort(nums);

        int ans = 1;
         for(int i = 0; i < nums.length; i++){
            if(nums[i] == ans){
                    ans++;
            }
        }
    return ans;
    }
}
*/

//Time Complexity : O(nlogn)
//Space Complexit : O(1)


//HashMap Approach : 
/*
public class _011_FirstMissingPositive {
    public int firstMissingPositive(int[] nums){
        
        HashSet<Integer> Set = new HashSet<>();
        for (int num : nums){
            set.add(num)
        }
        
        //Step 2 : Check integers starting from 1
        //we go up to nums.length + 1 because if the array is [1,2,3],
        //the answer is 4 (which is length + 1)
        for (int i = 1; i <= nums.length + 1; i++){
            if(!set.contains(i)){
                returns i; //Found the missing one
            }
        }

        return 1;

    }
}
*/



//Optimal Approach : Index as Hash Key
/*
public class _011_FirstMissingPositive {
    public int firstMissingPositive(int[] nums){
        int n = nums.length;

        int contains = 0;

        //Step 1 : Checking if 1 is present in the array
        for(int i = 0; i < n; i++){
            if(nums[i] == 1){
                contains++;
                break;
            }
        }

        if(contains == 0){
            return 1;
        }

        //Step 2 : Converting all negative instances greater than n to 1. We know 1 exists (from Step 1),
        //         so changing garbage to 1 is safe.
        for (int i = 0; i < n; i++) {
            if (nums[i] <= 0 || nums[i] > n) {
                nums[i] = 1;
            }
        }

        //Step 3 : going to first no. > 1 , taking it as index, and changing subsequent to -1
        for(int i = 0; i < n; i++){
            int a = Math.abs(nums[i]);

            if(a == n){
                nums[0] = -Math.abs(nums[0]);
            }
            else{
                nums[a] = -Math.abs(nums[a]);
            }
        }

        //Step 4 : Finding First missing positive
        for(int i = 1; i < n; i++){
            if(nums[i] > 0){
                return i;
            }
        }

        // Step 5: Check for value n (stored at index 0)
        if(nums[0] > 0){
            return n;
        }

        // If 1..n are all present, the answer is n+1
        return n+1;
    }
}

//Time Complexity: O(n)
//Space Complexity : O(1)
*/


//Optimal Approach 2 : Cyclic Sort
/*
Step 1 : Reorder the array using a Cyclic Sort. We iterate through the array and swap numbers to their correct
         positions: value x should be placed at index x-1. (We ignore negatives and numbers larger than the array size).

Step 2 : Iterate through the array again. The first index i where nums[i] != i + 1 is our answer. If all match, the answer is n + 1.
*/
public class _011_FirstMissingPositive {
    public int firstMissingPositive(int[] arr){

        for(int i = 0; i < arr.length; i++){
            while(arr[i] > 0 && arr[i] <= arr.length && arr[arr[i]-1] != arr[i]){
                int temp = arr[i];
                arr[i] = arr[temp -1];
                arr[temp -1] = temp;
            }
        }

        for(int i = 0; i < arr.length; i++){
            if(arr[i] != i + 1){
                return i + 1;
            }
        }

        return arr.length + 1;
    }
}

//Time Complexity: O(n)
//Space Complexity : O(1)
