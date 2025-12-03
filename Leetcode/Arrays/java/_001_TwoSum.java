/*
Problem Description : I am provided with an array and an target number. My 
                      goal is to find the numbers with the array such that they
                      sum up to the given target number.

                      e.g [2,3,4,5,6] target : 9    ans : [4,5],[3,6]




Approach : I am planning to use hash map to store the compliment of the numbers while 
           iterating through the array, wheneve a number requires a compliment, it will
           be checked in hash map, if it is present is returned else it iterates till the 
           end, if none is found that sums up to the target, we just return empty array
*/




    package Leetcode.Arrays.java;

    import java.util.HashMap;
    import java.util.Map;
//    import java.util.Arrays;
//    import java.util.Comparator;

    //Brute force approach A - Linear Search

    /*
    class TwoSum001 {
        public int[] twoSum(int[] nums, int target){

            for(int i = 0; i < nums.length; i++){
                int compliment = target - nums[i];

                for(int j = 0; j < nums.length; j++){
                    if(i != j && nums[j] == compliment){
                        return new int[] {i, j};
                    }
                }
            }
            return new int[] {};
        }
    }
    */

    //Brute force approach B - Linear search 
    /*
    class TwoSum001 {
        public int[] twoSum(int[] nums, int target){

            for(int i = 0; i < nums.length; i++){
                for(int j = 0; j < nums.length; j++){
                    if(nums[i] + nums[j] == target){
                        return new int[] {i, j};
                    }
                }
            }
            return new int[] {};
        }
    }

    Time Complexity : O(n2)
    Space Complexity : O(n)
    */

    /*
    //Brute force approach B : Sorting then applying Binary Search
        class TwoSum001 {
        public int[] twoSum(int[] nums, int target){

            int[][] arr = new int[nums.length][2];

            //store number + original index
            for (int i = 0; i < nums.length; i++){
                arr[i][0] = nums[i]; //value
                arr[i][1] = i;       //Index
            }

            Arrays.sort(arr, (a,b) -> Integer.compare(a[0], b[0]));   // a custom comparator sort using Timesort (for object arrays)
                                                                      // Merge Sort + insertion sort

            // Arrays.sort(arr, new Comparator<int[]>() {   //Elaboration of above lamda function
            //     public int compare(int[] a, int[] b){
            //         return Integer.compare(a[0], b[0]);
            //     }
            // });

            for(int i = 0; i < arr.length; i++){
                int complement = target - arr[i][0];
                int left = i + 1, right = arr.length - 1;

                //binary search 
                while(left <= right){
                    int mid = left + (right - left)/2;

                    if (arr[mid][0] == complement){
                        return new int[] { arr[i][1], arr[mid][1] };
                    } else if (arr[mid][0] < complement) {
                        left = mid + 1;
                    } else {
                        right = mid - 1;
                    }

                }
            }

            return new int[] {};
        }
    }

    Time Complexity : O(NlognN)
    Space Complexity : O(N2)

    */

    class TwoSum001 {
        public int[] twosum(int[] nums, int target){
            //Creating hashmap to store numbers and their indices
            Map<Integer, Integer> map = new HashMap<>();

            //Iterating through the array
            for(int i = 0 ; i < nums.length ; i++){
                //calculating the compliment of current number
                int compliment = target - nums[i];

                if(map.containsKey(compliment)){
                    return new int[] {map.get(compliment), i};
                }

            //otherwise adding the current number and it's index to the map
            map.put(nums[i],i);
        }

        //Return an empty array if no solution is found
        return new int[] {};
    }
}

class _001_TwoSum{
    public static void main(String[] args){

    TwoSum001 ob1 = new TwoSum001();

    int[] arr = new int[] {6,5,1,2,4,3};

    int[] result = ob1.twosum(arr, 9);
    System.out.println(java.util.Arrays.toString(result));
    }
}


//Time Complexity : O(n)
//Space Complexity : O(n)