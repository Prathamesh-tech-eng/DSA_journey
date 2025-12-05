'''
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
'''
#Brute Force :
'''
def valid_anagram(s, t) :
    if len(s) != len(t) : return False

    used = [False]*len(t)

    for i in range(len(s)):
        found = False

        for j in range(len(t)):
            if used[j] == False and s[i] == t[j]:
                used[j] = True
                found = True
                break
        
        if not found : return False
    return True

        Time Complexity : O(n2)
        Space Complexity : O(n)
    
'''


#Sorting Approach
'''
def valid_anagram(s,t):
    if len(s) != len(t) : return False
    return sorted(s) == sorted(t)


    Time Complexity : O(nlogn)
    Space Complexity : O(1)

'''

#Counting method
def valid_anagram(s,t):
    if len(s) != len(t) : return False

    freq = [0]*26

    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1   #characters are stored internally as numbers, and ord() lets us see that number.
        freq[ord(t[i]) - ord('a')] -= 1

    for count in freq:
        if count != 0: return False
        
    return True
    
#Time Complexity : O(n)
#Space Complexity : O(1)
