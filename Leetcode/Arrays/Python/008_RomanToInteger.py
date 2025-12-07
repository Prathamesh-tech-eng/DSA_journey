'''
Problem Description : We are provided with an roman integer, we need to convert them to decimal Integer.
                      e.g : CLXXI  O/P : 571

Problem Approach : There are 7 characters in roman numerical, whose combination is used and there are 6 exception condition where the smaller roman
                    character comes first before a larger character. I will store all this characters and exceptions as key and their decimal equivalent
                    integer as value in a hashmap. Then while iterating over a roman numerical, i will start with 2 characters at once, check if any exception
                    present in hashtable, if not, separate them and add their values, and do this till end and return the result.

Link : https://leetcode.com/problems/roman-to-integer/description/
'''

def roman_to_int(rmns):

    cnds = {    

        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    total = 0
    i = 0

    while i < len(rmns):
        # Check if next 2 characters form a valid subtractive pair
        if i + 1 < len(rmns) and rmns[i:i+2] in cnds:
            total += cnds[rmns[i:i+2]]
            i += 2
        else:
            total += cnds[rmns[i]]
            i += 1

    return total

#Time Complexity : O(n)
#Space Complexity : O(1)


#Substraction Logic
'''
def roman_to_int(rmns):

    cnds = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    total = 0
    i = 0

    for i in range(len(rmns)):
        if i + 1 < len(rmns) and cnds[rmns[i]] < cnds[rmns[i+1]]:
            total -= cnds[rmns[i]]

        else : 
            total += cnds[rmns[i]]
        
    return total
    '''


#Time Complexity : O(n)
#Space Complexity : O(1)


