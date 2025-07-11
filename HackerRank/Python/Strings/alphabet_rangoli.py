'''Problem Description : I am supposed to make a alphabet rangoli , you can view that on the link provide >_<
                         Link : https://www.hackerrank.com/challenges/alphabet-rangoli
                         
Approach : I will divide the problem into two parts upper and lower. And then i will apply for loop to both
           upper and lower. I will take input n, and create a width variable that will be 4*n-3. for total
           number of iterations, i will use the n in upper and n-2 in lower. and for the pattern 1 i.e "-" i will use formula :
           (width - pattern2_width)//2 on both sides left and right, and in the center will be the pattern 2
            I will create a arr consisting all characters from a-z, and then take out the list of charachters i need
            e.g if n =4 i will get lst = ['a','b','c','d'] and I will join them progressively after each iteration
            using "-".join() '''

import string
def print_rangoli_size(n):
    
    width = 4*n - 3
    p1 = "-"

    letters = list(string.ascii_lowercase)
    lst1 = letters[:n]                 #lst1 = ['a', 'b', 'c', 'd']      O(n)
    lst2 = lst1[::-1]                  #lst2 = ['d', 'c', 'b', 'a']      O(n)
    lst3 = []

   #Upper Part
    for i in range(n):                              #O(n)       i = 0 to 4 lst3 = [['d'], ['d', 'c'], ['d', 'c', 'b'], ['d', 'c', 'b', 'a']]  
        lst3.append(lst2[:i+1])                     #O(i+1)
        lst3[i].extend(lst1[n-i:])                  #O(i)
        p2 = "-".join(lst3[i])                      #O(n)
        p1_width = (width - len(p2))//2
        print((p1*p1_width) + p2 + (p1*p1_width))

    #Lower Part
    for i in range(n-2,-1,-1):                
        lst3.append(lst2[:i+1])
        p2 = "-".join(lst3[i])
        p1_width = (width - len(p2))//2
        print((p1*p1_width) + p2 + (p1*p1_width))

print_rangoli_size(10)

#Time Complexity : O(n^2)
#Space Complexity : O(n^2)