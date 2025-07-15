'''Problem Description : I am provided a string and integer n, I need to print each possible combination of size upto n each on next line
                         Link : https://www.hackerrank.com/challenges/itertools-combinations
                         
Approach : I will use itertools.combinations()'''

import itertools
A , n = input().split()
A = sorted(A)

for j in range(1,int(n)+1):
    for i in itertools.combinations(A, j):      
        print("".join(i))

#Time Complexity : O(C × k) where C = total combinations and k = avg length
#Space Complexity : O(1)
