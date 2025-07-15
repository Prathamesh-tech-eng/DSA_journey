'''Problem Descriptioin : I am provided with a,b and c. I need to print a^b and a^b%c
                          e.g a = 2  b = 5  c = 10   O/P : 32, 2
                          Link : https://www.hackerrank.com/challenges/python-power-mod-power

                          
Approach : I will use built in function in python i.e pow(a,b) and pow(a,b,c)
'''

a = int(input())
b = int(input())
c = int(input())

print(f"{pow(a,b)}\n{pow(a,b,c)}")

#Time Complexity : O(logb)
#Space Complexity : O(1)

