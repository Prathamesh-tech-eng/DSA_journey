package Leetcode.Arrays.java;

import java.util.Arrays;

/*
    Problelm Description : I am provided with an array, and i need to return an answer array where each index element has a value that is product of 
                           all other index values except itself. The solution strictly needs to be of O(n) time complexity. The use of division approach
                           is restricted.

                           e.g : [10, 20, 30, 40]   O/P : [24000, 12000, 8000, 6000]


    Problem Approach : Brute force mgiht have worked, where we would use two for loops and just find product for each index seperately, but it will cost
                       O(N2) time complexity. so we are avoiding that. Next is prefix and suffix approach. we will have pre consisting of product value of 
                       before target index and pro consisting of product of after index values. so each time we won't need to iterate to find the product. We 
                       can optimize it further by just creating a single array ans instead of creating seperate arrays for pre, postt and ans
*/

public class _006_ProductOFarrayExceptSelf {
    public int[] productExceptSelf(int[] nums){



    // Better Approach : Seperate arrays for each :
    /*
        int[] result = new int[nums.length];
        int[] pre = new int[nums.length];
        int[] post = new int[nums.length];

        pre[0] = 1;
        post[nums.length-1] = 1;

        for(int i = 1; i < nums.length; i++){
            pre[i] = nums[i-1] * pre[i-1];
        }

        for(int i =  nums.length - 2; i >= 0  ; i--){
            post[i] = nums[i+1] * post[i+1];
        }

        for(int i = 0; i < nums.length; i++){
            result[i] = pre[i] * post[i];
        }

        return result;

        // Time Complexity : O(3n) i.e O(n)
        // Space Complexity : O(n)

        */


        // Optimal Approach : only one array ans

        int[] result = new int[nums.length];
        Arrays.fill(result, 1);
        int pre = 1,  post = 1;

        for(int i = 0; i < nums.length; i++){
            result[i] = pre;
            pre = nums[i] * pre;
        }

        for(int i =  nums.length - 1; i >= 0  ; i--){
            result[i] = result[i] * post;
            post = nums[i] * post;
        }

        return result;

        // Time Complexity : O(2n) i.e O(n)
        // Space Complexity : O(1)

        
    }
}
