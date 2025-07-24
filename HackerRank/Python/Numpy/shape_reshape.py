'''Problem Description : I am provided a list, and I need to change it's dimension to 3*3
                        e.g 11 12 13 14 15 16   O/P :      [[11 12 13]
                                                            [14 15 16]
                                                            [17 18 19]]
                        Link : https://www.hackerrank.com/challenges/np-shape-reshape
                        
Approach : I will use numpy.reshape() to change the dimension dirctly and return it
'''

import numpy

print(numpy.reshape(list(map(int,input().split())), (3,3)))

#Time Complexity : O(n)
#Space Complexity : O(n)