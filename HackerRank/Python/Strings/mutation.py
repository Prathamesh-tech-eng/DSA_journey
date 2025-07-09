'''Problem Description : I am provided with a string, and my task is to replace a character at a specified position
                         eg. string = "Prathamesh" I/p : 5 h     O/p : "Prathhmesh"
                         link : https://www.hackerrank.com/challenges/python-mutations
                         
Approach : will use string slicing'''

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]      #O(p) + O(1) + O(n-p-1) = O(n)
    return string


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

#Time complexity : O(n)