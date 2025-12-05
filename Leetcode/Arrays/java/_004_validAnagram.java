
package Leetcode.Arrays.java;
//import java.util.Arrays;
/*
Problem Description : I am provided with two strings. And i need to check whether these 
                      two strings are anagram of each other. If they are , they will return
                      true, else false. Each and every character from one
                      string must be present in the other string, not less, not more.

                      e.g : I/P : code, ocde   O/P : True

Problem Approach : The problem can be solved by just iterating both strings, checking if the 
                   character from one string is present in other string or not. We can optimize it
                   by adding a condition : length of both the strings should be equal. Now for the
                   logic, i am planning to use array of size 26, which will store the frequecy of 
                   characters, for str1, we will do +1 for present characters and for str2 we will do \
                   -1 , so that an anagram will always have the array with all null values.
*/


public class _004_validAnagram {
    public boolean isAnagram(String s, String t){
    
    if (s.length() != t.length()) return false;
    
    //Brute Force 

    /*
    boolean[] used = new boolean[t.length()];

    for(int i = 0; i < s.length(); i++){

        char c = s.charAt(i);
        boolean found = false;

        for( int j = 0; j < s.length(); j++ ){
            if (!used[j] && s.charAt(i) == c){
                used[j] = true;
                found = true;
                break;
            }
        } 
        
        if (!found){
            return false; //couldn't find the matching char
        }
    }
    return true;

    Time Complexity : O(n2)
    Space Complexity : O(n)
*/       


   //Using Sorting Method
   /*
   char[] sArr = s.toCharArray();
   char[] tArr = t.toCharArray();

   Arrays.sort(sArr);
   Arrays.sort(tArr);

   return Arrays.equals(sArr, tArr);


   Time Complexity : O(nlogn)
   Space Complexity : O(n)
     */


    //using counting method
        if(s.length() != t.length()){
            return false;
        }

        // create an array to count character frequencies
        int[] charCount = new int[26]; // assuming only lowercase english letters


        for(int i = 0; i < s.length(); i++){
            charCount[s.charAt(i) - 'a']++;    //charAt(i) just extracts one letter at a time from the string
            charCount[t.charAt(i) - 'a']--;
        }

        //check if all counts are zero
        for(int count : charCount){
            if(count != 0){
                return false; 
            }
        }

        return true;
    }
}

//Time Complexity : O(n)
//Space Complexity : O(1)