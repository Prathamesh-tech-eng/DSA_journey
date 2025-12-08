package Leetcode.Arrays.java;

//import java.util.HashMap;
//import java.util.Map;

/*
Problem Descreption : we are provided with an order of lower case english alphabets, and we are also provided with an array of strings, whose order
                      we need to verify whether they follow they follow the specified order or not, if they do, we return true, else false.
                      e.g [hat, run, sink]  Order : [hdlfrigskabcdeijlmnopqtuvwxyz]  O/p : True

Problem Approach : We can create a hash table to store the character as key, as their position as value. Then we will just iterate over each string
                   in the array. In each iteration, we will check adjacent strings, and check the order using if - else. We can further optimize it by 
                   using int array instead of hashmap, as it is faster and uses less memory and we are also sure about the fixed size of the array i.e 26

Link : https://leetcode.com/problems/verifying-an-alien-dictionary/description/

*/


public class _009_VerifyingAlienDictionary {
    public boolean isAlienSorted(String[] words, String order){

        // Array Approach : 

        //Step 1 : Creating an array of fixed length
        int[] orderArr = new int[26];

        //Step 2 : Storing the characters orders in the array
        for(int i = 0; i < order.length(); i++){
            //Mapping Character 'a' to index 0 , 'b' to index 1 .....
            orderArr[order.charAt(i) - 'a'] = i; 
        }

        //Step 3 : Checking each adjacent string
        for(int i = 0 ; i < words.length - 1; i++){
            if (!checkOrder(words[i], words[i + 1], orderArr)) {
                return false;
            }
        }

        return true;

    }

        public boolean checkOrder(String s1, String s2, int[] orderArr){
            int len = Math.min(s1.length(), s2.length());

            for(int j = 0; j < len; j++){
                char char1 = s1.charAt(j);
                char char2 = s2.charAt(j);
                if(char1 != char2){
                    return orderArr[char1 - 'a'] < orderArr[char2 - 'a'];
                }
            }

            // if we reach here, one word is the prefix of other, so the shorter must come first
            return s1.length() <= s2.length();
               
        }
    }

//Time Complexity  : O(n)
//Space Complexity : O(1)

        





//Hash Table Approach : 
        /*

        //Step 1 : Creating a Hashmap
        Map<Character, Integer> map = new HashMap<>();


        //Step 2 : Store the content in hashmap
        for(int i = 0 ; i < order.length(); i++){
            map.put(order.charAt(i), i);
        }

        //Step 3 : Iterating over the strings and checking the order
        for(int i = 0; i < words.length-1; i++){
            for(int j = 0; j < words[i].length() ; j++){

                if( j >= s1[i].length()){
                    return false;
                }

                if (words[i].charAt(j) != words[i+1].charAt(j)){
                    int currWordChar = map.get(words[i].charAt(j));
                    int nextWordChar = map.get(words[i+1].charAt(j));
                    if(currWordChar > nextWordChar){
                        return false;
                    }
                    else {
                        break;
                    }            
                }
            }
        }

        return true;
    }
}

*/
//Time Complexity : O(n)
//Space Complexity : O(1)


