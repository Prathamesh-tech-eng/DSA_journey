'''
Problem Descreption : we are provided with an order of lower case english alphabets, and we are also provided with an array of strings, whose order
                      we need to verify whether they follow they follow the specified order or not, if they do, we return true, else false.
                      e.g [hat, run, sink]  Order : [hdlfrigskabcdeijlmnopqtuvwxyz]  O/p : True

Problem Approach : We can create a dictiornay to store the character as key, as their position as value. Then we will just iterate over each string
                   in the array. In each iteration, we will check adjacent strings, and check the order using if - else. 

Link : https://leetcode.com/problems/verifying-an-alien-dictionary/description/

'''
def _009_verifyingAlienDictionary( words, order):

    ''' 
    #Step 1 : create a dictionary
    alienOrder = {}

    #Step 2 : add the characters and their position as values
    for i in range(len(order)):
        alienOrder[order[i]] = i 
    '''

    # Step 1 & 2: Create dictionary (Using Dictionary Comprehension is faster!)
    alienOrder = {char: i for i, char in enumerate(order)}
    
    #Step 3 : Iterating over the dictionary 
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i+1]

        # Check first N characters
        for j in range(min(len(word1), len(word2))):
            # If characters are different, check order
            if word1[j] != word2[j]:
                if alienOrder[word1[j]] > alienOrder[word2[j]]:
                    return False
                # If we found a valid order, we stop checking this pair
                break
        else:
            if len(word1) > len(word2):
                return False
                
    return True

#Time Complexity : O(n)
#Space Complexity : O(1)


'''
Note : We are not using list here, unlike in java, where using arrays instead of hashmap in this problem gave us more optimized solution. But
       in case of python , in this problem it is not same. the reason that array was faster in java is because java treats char as number (integers)
       so 'c' - 'a' becomes a simple substraction (99 - 97 = 2). It happens instantly in the CPU level. But Python doesn't have such "Primitive
       char" type. A character is just a string of length 1 and to do math on these characters in python, we have to use ord(), i.e ord('c') - ord('a')
       and calling this function for every character comparison adds overhead, that cancels out the speed benefit of using list of size 26 .
'''