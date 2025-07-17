'''Problem Description : I have been provided date : DD MM YYYY , and need to identify the day
                         e.g : 12 02 2005    O/P : Saturday
                         Link : https://www.hackerrank.com/challenges/calendar-module
                         
Approach : I will the built in function in python
'''

import datetime

date = input()
dt = datetime.datetime.strptime(date, "%m %d %Y")
print(dt.strftime("%A").upper())

#Time Complexity : O(1)
#Space Complexity : O(1)

'''
dt = datetime.datetime.strptime(date, "%m %d %Y")
%m %d %Y == 02 12 2005
%m %d %y == 02 12 05
%m-%d-%Y == 02-12-2005

dt.strftime("%A")
%A : Saturday
%a : Sat

'''