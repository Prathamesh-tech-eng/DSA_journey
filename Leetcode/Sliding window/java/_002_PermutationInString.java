/*
Problem Description : we are provided with two strings, we need to check if s1 in any permutation is present in s2. If yes , return True
                      else False.
                      e.g : s1 : put  s2 : throughput  O/P : True

Problem Approach : We can just apply brute force by voluntarily checking if each of the s1 is present in s2 or not, that will cost us O(n2)
                   Time Complexity. We can improve that by using the Hash map to store the character of the string s1 and their frequencies,
                   Then we create a hash map of same size for s2, where we check if we have same hashmap, if not, we slide the window i.e
                   we remove initial element, and add next element and recheck if it is identical to s1, if yes we return true, else we 
                   continue. We can further optimize this by using array of fixed size 26 to store the frequencey which will give us an
                   constant space complexity.

Link : https://leetcode.com/problems/permutation-in-string/
*/

//Using HashMap

//import java.util.HashMap;
//import java.util.Map;

/*
public class _002_PermutationInString {
    public boolean checkInclusion(String s1, String s2) {
        if (s1 == null || s2 == null) return false;
        int n1 = s1.length();
        int n2 = s2.length();
        if (n1 > n2) return false;
        if (n1 == 0) return true;

        // build frequency map for s1
        Map<Character, Integer> need = new HashMap<>();
        for (char c : s1.toCharArray()) {
            need.put(c, need.getOrDefault(c, 0) + 1);
        }

        // initial window (first n1 chars of s2)
        Map<Character, Integer> window = new HashMap<>();
        for (int i = 0; i < n1; i++) {
            char c = s2.charAt(i);
            window.put(c, window.getOrDefault(c, 0) + 1);
        }

        // matches = how many characters currently have counts equal to need
        int matches = 0;
        for (Map.Entry<Character, Integer> e : need.entrySet()) {
            if (window.getOrDefault(e.getKey(), 0).intValue() == e.getValue().intValue()) {
                matches++;
            }
        }
        if (matches == need.size()) return true;

        // slide the window
        for (int i = 0; i < n2 - n1; i++) {
            char right = s2.charAt(i + n1); // entering char
            char left = s2.charAt(i);       // leaving char

            // add right
            int beforeRight = window.getOrDefault(right, 0);
            Integer needRight = need.get(right);
            if (needRight != null && beforeRight == needRight) {
                // right previously matched need, will change
                matches--;
            }
            window.put(right, beforeRight + 1);
            if (needRight != null && window.get(right).intValue() == needRight.intValue()) {
                matches++;
            }

            // remove left
            int beforeLeft = window.getOrDefault(left, 0);
            Integer needLeft = need.get(left);
            if (needLeft != null && beforeLeft == needLeft) {
                // left previously matched need, will change
                matches--;
            }
            if (beforeLeft == 1) {
                window.remove(left);
            } else {
                window.put(left, beforeLeft - 1);
            }
            if (needLeft != null && window.getOrDefault(left, 0).intValue() == needLeft.intValue()) {
                matches++;
            }

            if (matches == need.size()) return true;
        }

        return false;
    }
}

*/

    //Time Complexity : O(n)
    //Space Complexity : O(n)


public class _002_PermutationInString {
    public boolean checkInclusion(String s1, String s2){
        if(s1.length() > s2.length()){
            return false;
        }

        //Step 1 : Creatign arrays to store frequenceis
        int[] s1map = new int[26];
        int[] s2map = new int[26];

        //step 2 : Initailizing frequency maps for s1 and the first window of s2
        for (int i = 0; i < s1.length(); i++){
            s1map[s1.charAt(i) - 'a']++;
            s2map[s2.charAt(i) - 'a']++;
        }

        //step 3 : Sliding the Window through s2 and comparing the maps
        for(int i = 0; i < s2.length() - s1.length(); i++){
            if(matches(s1map, s2map)){
                return true;
            }
            s2map[s2.charAt(i + s1.length()) - 'a']++;  //Add new character to the windo
            s2map[s2.charAt(i) - 'a']--;        //Remove old character form the window
            
        }

        //Step 4 : Check the Last Window
        return matches(s1map, s2map);
    }


    private boolean matches(int[] s1map, int[] s2map){
        for(int i = 0; i  < 26; i++){
            if(s1map[i] != s2map[i]){
                return false;
            }
        }
        return true;
    }
}
    //Time Complexity : O(n)
    //Space Complexity : O(1)


//micro Optimization
/* 
public class _002_PermutationInString {
    public boolean checkInclusion(String s1, String s2){

        if (s1 == null || s2 == null) return false;

        if(s1.length() > s2.length()){
            return false;
        }

        if (n1 == 0) return true;

        //Step 1 : Creatign arrays to store frequenceis
        int[] s1map = new int[26];
        int[] s2map = new int[26];

        //step 2 : Initailizing frequency maps for s1 and the first window of s2
        for (int i = 0; i < s1.length(); i++){
            s1map[s1.charAt(i) - 'a']++;
            s2map[s2.charAt(i) - 'a']++;
        }

        //step 3 : Sliding the Window through s2 and comparing the maps
        int matches = 0;

        for(int i = 0; i < 26; i++){
            if(s1map[i] == s2map[i]){
                matches++;
            }
        }

        for(int i = 0; i < s2.length() - s1.length(); i++){
            if(matches == 26){
                return true;
            }

            int right = s2map[s2.charAt(i + s1.length()) - 'a']++;  //Add new character to the windo
            int left = s2map[s2.charAt(i) - 'a']--;        //Remove old character form the window
            
            //add right char
            if (s2map[right] == s1map[right]) matches--;
            s2map[right]++;
            if (s2map[right] == s1map[right]) matches++;

            //remove left char
            if (s2map[left] == s1map[left]) matches--;
            s2map[left]++;
            if (s2map[left] == s1map[left]) matches++;


        }

        return matches == 26;
    }
}

*/

    //Time Complexity : O(n)
    //Space Complexity : O(1)
