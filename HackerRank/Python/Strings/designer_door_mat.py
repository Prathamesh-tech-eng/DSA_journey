'''Problem Description : I am supposed to print the provided design , visit the link to view it or run the code >_<
                         link : https://www.hackerrank.com/challenges/designer-door-mat
                         
Approach : I will divide the design into three parts, upper, middle and lower portions, and will use for loop to upper and lower
           . There is an increase in ".|." by odd , so using the 2*i-1 for the odd increment, and subtracting this from the design 
             width. the obatined result should be divided by two to get "-" on both sides, same goes for lower part, but the only 
             change will be in range(), it will be reverse'''

N, M = input().split()
N = int(N)
M = int(M)
a, b = "-", ".|."

half = (N - 1)//2
#Upper Part
for i in range(half):                  #O(N/2 * M) == O(N * M)
    mid = 2*i + 1
    outer = (M - 3*mid)//2
    print((a * outer) + (b * mid) + (a * outer))

#middle part                           #O(M)
middle = (M-7)//2
print((a * middle) + "WELCOME" + (a * middle))

#Lower Part                            #O(N/2 * M) == O(N * M)
for i in range(half-1, -1, -1):
    mid = 2*i + 1
    outer = (M - 3*mid)//2
    print((a * outer) + (b * mid) + (a * outer))


#Time Complexity : O(N*M)
#Space Complexity : O(1)
    