'''Problem Description : I am provided with a sentence , and I need to convert all the lowercase characters into uppercase and 
                         all uppercase characters to lowercase. 
                         e.g : I am Prathamesh   O/p : i AM pRATHAMESH
                         Link : https://www.hackerrank.com/challenges/swap-case
                         
Approch : I will use isupper() and islower() to identify uppercase and lowercase characters and convert them using upper() and
          lower(). I will iterate through the strings and check each  character and append the changed character into a new string
          '''

def swap_case(s):
    w = []
    for i in s:                                       #O(n)
        if i.isupper() : w.append(i.lower())          #O(1)
        else : w.append(i.upper())                    #O(1)
    result = ''.join(w)                               #O(n)
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#Time complexity : O(n)
#Space complexity : O(n)