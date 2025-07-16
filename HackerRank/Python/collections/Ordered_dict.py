'''Problem Description : I am given a list of n items with their price which is record of sold items to consumers. My task is to 
                         to print item name and it's net price according to it's first occurence
                         
                         Link : https://www.hackerrank.com/challenges/py-collections-ordereddict
                         
Approach : I will use if else to identify the item name add add in the dictionary and in the end i will use built in function 
           collection.ordered_dicy() to print it according to it's occurences.
           '''

import collections 
record = {}

n = int(input())
instruction, key, value = 0,0,0
for i in range(n):
    instruction = list(input().split())
    if len(instruction) > 2:
        key = " ".join(instruction[:2])
        value = int(instruction[2])
    else : 
        key = instruction[0]
        value = int(instruction[1])
    if key in record: 
        record[key] += value
    else : 
        record[key] = value
 
for i in collections.OrderedDict(record).items():
    print(" ".join(map(str, i)))


#Time Complexity : O(n + k)
#Space Complexity : O(k)


'''
from collections import OrderedDict

od = OrderedDict()
od["apple"] = 2
od["banana"] = 5
od["cherry"] = 3

for key, value in od.items():
    print(key, value)

    
Output:
apple 2
banana 5
cherry 3
'''



