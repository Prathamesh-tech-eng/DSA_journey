'''Problem Description : I am given two numbers a and b. I need to do a/b, and if an error occurs, i need to print the error code
                         e.g : 9/0   0/P : Error Code: integer division or modulo by zero
                         Link : https://www.hackerrank.com/challenges/exceptions
                         
Approach : I will use try catch, so that if an error occurs, i can easily print the error code
'''

n = int(input())

for i in range(n):
    a,b = input().split()
    try : 
        print(int(a)//int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)

#Time Complexity : O(n)
#Space Complexity : O(1)