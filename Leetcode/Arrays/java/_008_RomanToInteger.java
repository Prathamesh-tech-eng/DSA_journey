package Leetcode.Arrays.java;

import java.util.HashMap;
import java.util.Map;
/*
Problem Description : We are provided with an roman integer, we need to convert them to decimal Integer.
                      e.g : CLXXI  O/P : 571

Problem Approach : There are 7 characters in roman numerical, whose combination is used and there are 6 exception condition where the smaller roman
                    character comes first before a larger character. I will store all this characters and exceptions as key and their decimal equivalent
                    integer as value in a hashmap. Then while iterating over a roman numerical, i will start with 2 characters at once, check if any exception
                    present in hashtable, if not, separate them and add their values, and do this till end and return the result.

Link : https://leetcode.com/problems/roman-to-integer/description/
*/


public class _008_RomanToInteger {
    static Map<String, Integer> values = new HashMap<>();

    static {
        values.put("I", 1);
        values.put("V", 5);
        values.put("X", 10);
        values.put("L", 50);
        values.put("C", 100);
        values.put("D", 500);
        values.put("M", 1000);
        values.put("IV", 4);
        values.put("IX", 9);
        values.put("XL", 40);
        values.put("XC", 90);
        values.put("CD", 400);
        values.put("CM", 900);
    }

    public int romanToInt(String s){
        int sum = 0;
        int i = 0;


    // Substraction Logic
    /*
        for( i = 0 ; i < s.length(); i++){
            int current = values.get(String.valueOf(s.charAt(i)));

            if(i + 1 < s.length()){
                int next = values.get(String.valueOf(s.charAt(i)));

                if(current < next){      
                    sum -= current;
                    continue;   
                }
            }

            sum += current;

        return sum;

        //time Complexity : O(n)
        //Space Complexity : O(1)
*/



// 2 Symbol Logic.
        while (i < s.length()){
            if(i < s.length()){
                String twoSymbol = s.substring(i, i+2);
                if(values.containsKey(twoSymbol)){
                    sum += values.get(twoSymbol);
                    i+=2;
                    continue;
                }
            }

            String oneSymbol = s.substring(i, i+1);
            sum += values.get(oneSymbol);
            i+=1;
        }
        return sum;
    }
}

//time Complexity : O(n)
//Space Complexity : O(1)
