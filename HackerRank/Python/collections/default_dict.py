'''Problem Description : I am provided two list A and B containing characters. I need to to find the position of each elements from B
                         in A. If the character is not present in A, I need to print -1
                         e.g : A = bcbcdd  B = bcde  O/P : 1 3
                                                           2 4
                                                           5 6
                                                           -1
                                                           
                        Link : https://www.hackerrank.com/challenges/defaultdict-tutorial
                        
Approach : I will use the built in funtion defacult_dict and create a dictionary with default value as their index using enumerate funtion
           . I will use for loop to iterate through B
           '''
from collections import defaultdict
A_size, B_size = map(int, input().split())        
A = []

for i in range(A_size):                            #O(A_size)
    A.append(input())
    
B = defaultdict(list)

for idx, char in enumerate(A, start=1):             #O(A_size)     and  enumerate(A) loop = O(A_size)
    B[char].append(idx)
    

for i in range(B_size):                             #O(B_size × K)
    c = input()
    if c in B:
        print(" ".join(map(str, B[c])))
    else :
        print(-1)

#Time complexity : O(A_size + K * B_size)
#Space complexity : O(A_size)


'''Default_dict : 
from collections import defaultdict

group = defaultdict(list)
pairs = [("a", 1), ("a", 2), ("b", 3)]

for key, value in pairs:
    group[key].append(value)

print(group)  # {'a': [1, 2], 'b': [3]}


enumerate : 

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

Output:

0 apple
1 banana
2 cherry
'''