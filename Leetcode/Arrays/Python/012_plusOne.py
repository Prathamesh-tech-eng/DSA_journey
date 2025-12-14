'''
Problem Description : we are provided an integer represented as array of digits and we need to increment the integer by one and return the resulting
                      array of digits.
                      e.g : 139 + 1 = 140   I/P -   [1,3,9]  O/P - [1,4,0]

Problem Approach : The 1 would only increment the n-1th element of the array if the digits[n-1] <= 8, if it is 9 we just replace digits[n-1] = 0

Link : https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=array

'''



# The Optimal Approach : 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
    
#Time Complexity : O(n)
#Space Complexity : O(1)
    

# Correct but unacceptable approach : 
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = int("".join(map(str, digits)))
        plusOne = num + 1

        x = str(plusOne)
        lst = []

        for char in x:
            lst.append(int(char))

        return lst'''
#Time Complexity : O(n)
#Space Complexity : O(n)

#Why :
'''
interviewers don’t like this approach

The problem expects digit-wise manipulation, not number conversion.

Fails for very large inputs , Python supports big integers, but: Other languages overflow

Interviewers want a language-agnostic solution

Extra memory usage - Creates multiple intermediate objects

Big integer conversions are expensive internally
'''