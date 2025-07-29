'''Problem Description : I am provided an array A of Size N, I need to reverse it and print the result.
                         e.g : 11 22 33 44      O/P : 44 33 22 11
                         Link : https://www.hackerrank.com/challenges/arrays-ds
                         
Approach : I will use string slicing to reverse the array and print it.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()


#Time Complexity : O(n)
#Space Complexity : O(n)

# I can use loop to further reduce the space usage
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    left, right = 0, len(a)
    while left < right :
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()


#Time Complexity : O(n)
#Space Complexity : O(1)