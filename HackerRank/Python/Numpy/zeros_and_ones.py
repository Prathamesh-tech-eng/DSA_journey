'''Problem Description : I am provided a shape of array in space seperated forms and i am supposed to print arrays of zeros and ones
                         from the provided dimension and type.
                         e.g 2 2 2  O/P :   [[0 0]     
                                            [0 0]]
                                            
                                            [[0 0]
                                            [0 0]]
                                            
                                            [[1 1]
                                            [1 1]]
                                            
                                            [[1 1]
                                            [1 1]]

                        Link : https://www.hackerrank.com/challenges/np-zeros-and-ones


Approach : I will use tuple to convert user input into a shape that numpy expects for multidimensional arrays
            built in python i.e np.ones and np.zeros and print them            
                        '''
import numpy as np

shape = tuple(map(int, input().split()))
print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))

#Time Complexity : O(n)  where n = total no. of elements in the array
#Space Complexity : O(n)