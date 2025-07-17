'''Problem Description : I am Provided a list, i need to perform append, pop, popleft and appendleft() using an dequeue
                         Link : https://www.hackerrank.com/challenges/py-collections-deque
                         
Approach : Will use the python built in functions .pop(), .appendleft(), append(), popleft()
'''

import collections
n = int(input())
lst = collections.deque()

for i in range(n):
    instruction = input().split()
    if instruction[0] == 'append':
        lst.append(int(instruction[1]))
    elif instruction[0] == 'appendleft' :
        lst.appendleft(int(instruction[1]))
    elif instruction[0] == 'pop':
        lst.pop()
    elif instruction[0] == 'popleft':
        lst.popleft()

print(" ".join(map(str, lst)))
    

#Time Complexity : O(n)
#Space Complexity : O(n)