'''Problem Discription : I am given instruction out of 7 commands : insert x y, reverse, sort, pop, print, append x, remove x
                         and i am supposed to pring resulting list after performing provided operations on the list
                         link : https://www.hackerrank.com/challenges/python-lists
                         
Approach : I will split the input into command and args, and then use if else to identify the instruction and perform operation'''

N = int(input())

lst = []
    
for _ in range(N):
    
    instruction = input().strip().split()  #O(n) + O(n) + O(n) = O(3n) = O(n)
    command = instruction[0]
    args = instruction[1:]
    
    if command == "insert":
        lst.insert(int(args[0]),int(args[1]))
    elif command == "append":
        lst.append(int(args[0]))
    elif command == "print":
        print(lst)
    elif command == "remove":
        lst.remove(int(args[0]))
    elif command == "sort":
        lst.sort()
    elif command == "pop":
        lst.pop(-1)
    elif command == "reverse":
        lst.reverse()

#Time Complexity : O(n)