package Leetcode.Arrays.java;

//import java.util.ArrayList;
/*
Problem Description : we are provided with an array, and an integer k. We need to find the the top k most frequently occuring elements among the given
                      array. 
                      e.g : [11,12,11,12,11,24]   k = 2, O/P: [11,12]

Problem Approach : we can just brute force it by iterating each element, taking their count, and then returning the k most frequent elements. To optimize
                   we can use Hash map to store the elements and it's frequency. this will significantly reduce the time complexity and then we can just 
                   sort the hash values and return the k values. We can further optimize it by using heap (priority queue) instead of sorting by defining 
                   array of only k size.
*/
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
// import java.util.stream.Collectors;
// import java.util.List;
// import java.util.LinkedHashMap;
// import java.util.Comparator;
public class _007_TopKfrequentElements {
    public int[] topKFrequent(int[] nums, int k){


        //Using HahMap + Bucket Solution
        /*
        // Step 1 : Create Hashmap
        Map<Integer, Integer> map = new HashMap<>();
        for(int num : nums){
            map.put(num, map.getOrDefault(num, 0)+1);
        }


        //Step 2 : Create Bucktes : index = frequency, value = list fo numbers with that frequency
        List<Integer>[] buckets = new List[nums.length + 1];
        for (Map.Entry<Integer, Integer> entry : map.entrySet()){
            int num = entry.getKey();
            int f = entry.getValue();
            if(buckets[f] == null){
                buckets[f] = new ArrayList<>();
            }
            buckets[f].add(num);
        }

        //Step 3 : Collecting the highest frequency bucket downwards
        int[] ans = new int[k];
        int idx = 0;
        for(int f = buckets.length - 1; f >= 0 && idx <k; f--){
            if(buckets[f] != null){
                for (int num : buckets[f]){
                    ans[idx++] = num;
                    if (idx == k) break;
                }
            }
        }

        return ans;

        */
        //  Time Complexity : O(n)
        //  Space Complexity : O(n)

       
      
        //Using HasMap + Sorted Array
        /*
        if(k == nums.length){
            return nums;
        }

        Map<Integer, Integer> map = new HashMap<>();  //creating Hashmap to store elements and their frequencies.
        
        for(int n:nums){
            map.put(n, map.getOrDefault(n, 0) + 1);   //get the current count of n and if n does NOT exist in the map yet, return 0
        }

        // Sorted hashmap by value in descending order
        LinkedHashMap<Integer, Integer> sortedMap = map.entrySet()
                    .stream()
                    .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                    .collect(Collectors.toMap(
                        Map.Entry::getKey,
                        Map.Entry::getValue,
                        (e1, e2) -> e1,
                        LinkedHashMap::new
                    ));
        
        int[] ans = new int[k];
        int index = 0;

        for(int key : sortedMap.keySet()){
            if(index == k) break;
            ans[index++] = key;  
        }

        return ans;

        */

        //Time Complexity : O(nlogn)
        //Space Complexity : O(n)


        
        //Using HashMap + Priority Queue (Heap)

        if(k == nums.length){
            return nums;
        }

        Map<Integer, Integer> map = new HashMap<>();  //creating Hashmap to store elements and their frequencies.
        
        for(int n:nums){
            map.put(n, map.getOrDefault(n, 0) + 1);   //get the current count of n and if n does NOT exist in the map yet, return 0
        }

        Queue<Integer> heap = new PriorityQueue<>(
            (a,b) -> map.get(a) - map.get(b)
        );

        /*
        ---------------
        new PriorityQueue<>(new Comparator<Integer>() {   //heap becomes sorted by frequency
            @Override
            public int compare(Integer a, Integer b) {
                return map.get(a) - map.get(b);
            }
        });
        -------------
        */
        
        for(int n : map.keySet()){
            heap.add(n);                    //push number into heap
            if(heap.size() > k){            //if heap holds more than k numbers
                heap.poll();                //remove the least frequent element
            }
        }
    
        int[] ans = new int[k];
        for(int i = 0 ; i < k; i++){
            ans[i] = heap.poll();         //Each poll() gives the next most frequent remaining element
        }

        return ans;

        //Time Complexity : O(nlogk)
        //Space Complexity : O(n)     (map + heap + ans)

    }
}
