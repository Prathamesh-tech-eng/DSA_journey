'''
Problem Description : we are provided with two strings, we need to check if s1 in any permutation is present in s2. If yes , return True
                      else False.
                      e.g : s1 : put  s2 : throughput  O/P : True

Problem Approach : We can just apply brute force by voluntarily checking if each of the s1 is present in s2 or not, that will cost us O(n2)
                   Time Complexity. We can improve that by using the dictionary to store the character of the string s1 and their frequencies,
                   Then we create a dictionary of same size for s2, where we check if we have same dictionary, if not, we slide the window i.e
                   we remove initial element, and add next element and recheck if it is identical to s1, if yes we return true, else we 
                   continue. We can further optimize this by using array of fixed size 26 to store the frequencey which will give us an
                   constant space complexity.

Link : https://leetcode.com/problems/permutation-in-string/
'''

def check_inclusion_lowercase(s1: str, s2: str) -> bool:

    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        return False
    if n1 == 0:
        return True

    a = [0] * 26
    b = [0] * 26
    for i in range(n1):
        a[ord(s1[i]) - 97] += 1
        b[ord(s2[i]) - 97] += 1

    matches = sum(1 for i in range(26) if a[i] == b[i])

    for i in range(n2 - n1):
        if matches == 26:
            return True

        right = ord(s2[i + n1]) - 97
        left = ord(s2[i]) - 97

        # add right char
        if b[right] == a[right]:
            matches -= 1
        b[right] += 1
        if b[right] == a[right]:
            matches += 1

        # remove left char
        if b[left] == a[left]:
            matches -= 1
        b[left] -= 1
        if b[left] == a[left]:
            matches += 1

    return matches == 26

# Time Complexity : O(n)
# Space Complexity : O(n)
