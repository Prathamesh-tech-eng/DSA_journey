'''Problem Description : I am provided marksheet, which has enteries of marks otained by students in three subjects , I will be provided 
                         a student ID and I need to find his average marks in the three subjects.
                         e.g : Student ID → 1    2    3    4    5
                              Subject 1   | 98   88   74   67   80
                              Subject 2   | 98   78   82   70   70
                              Subject 3   | 83   95   99   83   62
                                          |______________________________
                              Average       93.0 87.0 85.0 73.3 70.7
                              
                              
                              Link : https://www.hackerrank.com/challenges/zipped

Approach : I will use the built in function zip() to create a different list for each student and then use that list to find the 
           average
                              '''

size,n = map(int, input().split())
sub = []

for i in range(n):
    sub.append(list(map(float, input().split())))
sub = list(zip(*sub))

for i in range(size):
     x = sum(sub[i])/n
     print(f"{x:.1f}")


#Time Complexity : O(n * size)
#Space Complexity : O(n * size)


