'''Problem Description : I am provided a list of number, i need to print reverse of the list using numpy
                         e.g : [1, 2, 3, 4, 5]   O/P : [5, 4, 3, 2, 1]
                         Link : https://www.hackerrank.com/challenges/np-arrays
                         
Approach : I will use np.array to convert the list into array and will print the array in reverse
'''

import numpy

def arrays(arr):
    return numpy.array([float(num) for num in arr][::-1])
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


#Time Complexity  :  O(n)
#Space Complexity : O(n)
