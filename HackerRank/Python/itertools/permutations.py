'''Problem Description : I am provided a string and integer n, I need to provide permutation of size n , each on new line
                         e.g : 'two' 3        O/P : two
                                                    tow
                                                    otw
                                                    owt
                                                    wto
                                                    wot
                        Link : https://www.hackerrank.com/challenges/itertools-permutations
                         

                        Approach : I will use itertools.permutations() for finding the permutations of n sizes '''

import itertools

A, n = input().split()
B = sorted(list(itertools.permutations(A, int(n))))    #Total permutations =  P(len(A), n) = len(A)! / (len(A) - n)!
                                                       # sorting : O(PlogP)
for i in B:                                            #O(n)
    C = list(i)
    print("".join(C))

#Time complexity :  O(P × log P × n)
#Space Complexity : O(p * n)

##Could be more optimal : I will not use list
A, n = input().split()
for i in sorted(itertools.permutations(A, int(n))):
    print("".join(i))

#Time Complexity : O(P × n + P × log P) = O(P × (n + log P))
#Space Complexity : O(p * n)