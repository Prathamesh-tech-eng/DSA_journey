'''
Problem description ; I am provided with a list of strins, and I am 
                      supposed to return a list of anagrams from the provided list.
                      e.g ['rat', 'put', 'tar']  O/P : [['rat', 'tar'], ['put']]  (could be in any order)

Problem Approach : we can linearly search each string if it is anagram or not, and then create a list. To 
                   optimize it, we can use another duplicate array, sort it, find the indices with equal values
                   and return those indices in the list. The most optimal approach will be to use hashmap. We will 
                   create a hashmap of 26 size, with characters representing key, so all the anagrams will end up with
                   same keys, we can just return them there.

'''

#Brute Force:
'''
def groupAnagram(strs) : 
    result = []
    used = [False]*len(strs)

    for i in range(len(strs)):

        if used[i]:
            continue

        used[i] = True
        group = [strs[i]]

        for j in range(i+1, len(strs)):
            if not used[j] and isAnagram(strs[i], strs[j]) :
                group.append(strs[j])
                used[j] = True

        result.append(group)
    return result


def isAnagram(a, b):
    return sorted(a) == sorted(b)

'''
#Time complexity : O(n2. klogk)
#Space Complexity : O(n)



#sorting based Approach (using sorting method to obtian keys) : 
'''
from collections import defaultdict

def groupAnagram(strs):
    groups = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        groups[key].append(word)

    return list(groups.values())

'''
#Time Complexity : O(n.klogk)
#Space Complexity : O(n)


#Optimal Approach:  (using count method to obtain keys)
from collections import defaultdict

def groupAnagram(strs):
    groups = defaultdict(list)  #automatically creates a default value when a key is missing, no need to check if the key exists

    for word in strs:
        #frequency count of 26 letters (since Lowercase)
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1

        key = tuple(count)
        groups[key].append(word)

    return list(groups.values())

#Time Complexity : O(n.k)
#Space Complexity : O(n)