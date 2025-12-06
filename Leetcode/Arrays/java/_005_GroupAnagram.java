package Leetcode.Arrays.java;

import java.util.*;
/*
Problem description ; I am provided with a list of strins, and I am 
                      supposed to return a list of anagrams from the provided list.
                      e.g ['rat', 'put', 'tar']  O/P : [['rat', 'tar'], ['put']]  (could be in any order)

Problem Approach : we can linearly search each string if it is anagram or not, and then create a list. To 
                   optimize it, we can use another duplicate array, sort it, find the indices with equal values
                   and return those indices in the list. The most optimal approach will be to use hashmap. We will 
                   create a hashmap of 26 size, with characters representing key, so all the anagrams will end up with
                   same keys, we can just return them there.
*/

class _005_GroupAnagram {
    public List<List<String>> groupAnagrams(String[] strs){
       

        //Brute Force Approach : 
        /*
        List<List<String>> result = new ArrayList<>();
        boolean[] used = new boolean[strs.length];

        for(int i = 0; i < strs.length; i++){
            if (used[i]) continue; //already in same group

            List<String> group = new ArrayList<>();
            group.add(strs[i]);
            used[i] = true;

            //Compare strs[i] with all later words
            for (int j=i+1 ; j < strs.length; j++){
                if (!used[j] && isAnagram(strs[i], strs[j])){
                    group.add(strs[j]);
                    used[j] = true;
                }
            }

            result.add(group);
        }
        return result;
    }

    private boolean isAnagram(String a, String b){ //helper to check if two strings are anagrams
        
        if (a.length() != b.length()) return false;

        char[] arr1 = a.toCharArray();
        char[] arr2 = b.toCharArray();

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        return Arrays.equals(arr1,arr2);
    }


    Time Complexity : O(n2.klogk)
    Space Complexity : O(n)

    */


    // Best Approach : 
        
        if (strs == null || strs.length == 0) {  //Handle empty input by returning empty array
            return new ArrayList<>();
        }

        Map<String, List<String>> ansMap = new HashMap<>();

        int[] count = new int[26];

        for(String s : strs){
            Arrays.fill(count, 0);
            for(char c : s.toCharArray()){
                count[c - 'a']++;
            }

            StringBuilder sb = new StringBuilder();

            for(int i = 0 ; i < 26; i++){
                sb.append('#');   //here # is used to avoid confusion between numbers
                sb.append(count[i]);
            }

            String key = sb.toString();  //converting sb(right now is a mutable StringBuilder object) into immutable string
            ansMap.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
            /*
                    List<String> list = ansMap.get(key);
                    if (list == null) {
                        list = new ArrayList<>();
                        ansMap.put(key, list);
                    }
                    list.add(s);
            */
        }

        return new ArrayList<>(ansMap.values());
        
    }
}

// Time Complexity : O(n*k)
// Space Complexity : O(n)