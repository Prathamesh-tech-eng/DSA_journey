'''Problem Description : I am provided four integers a,b,c and d . And I need to find out a^b + c^d
                         Link : https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes
                         
Approach : I will use pow(a,b) to get a^b and same goes for c^d and will print their sum
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(f"{pow(a,b) + pow(c,d)}")


##OR

a, b, c, d = (int(input()) for _ in range(4))
print(pow(a, b) + pow(c, d))


#Time complexity : O(logb + logd)
#Space complexity : O(1)