'''Problem desription : I am provided with list of student ID, marks, class and name. I need to print the average marks of the list 
                        corrected to 2 digits.
                        link : https://www.hackerrank.com/challenges/py-collections-namedtuple
                        
                        
Approach : I will use store this in a named_tuple and then calculate the average marks'''

from collections import namedtuple

data = []
n = int(input())

class_data = namedtuple('class_data' , input().split())
avg = 0
for i in range(n):
    data = class_data(*input().split())
    avg += int(data.MARKS)

print(f"{avg/n:.2f}")
  

#Time Complexity : O(n)
#Space Complexity : O(1)


#More compact version but with same complexity : 
from collections import namedtuple
n, fields = int(input()), input().split()
Student = namedtuple('Student', fields)
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n:.2f}")


'''
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p)

Output:

Point(x=10, y=20)
'''