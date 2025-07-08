'''Problem Discription : I am provided with a list of students , with their marks in subjects, I need to calculate
                         average of marks of a specified student. eg. krishna = 23, 45, 56   gaytri = 13, 47, 89  
                         krishna o/p : 41.33
                         link : https://www.hackerrank.com/challenges/finding-the-percentage
                         
Approach : I will use sum function on respective list of marks of specified students and divide by length of list and print it'''



n = int(input())
student_marks = {}
for _ in range(n):                      #O(n*m)
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
    
student_avg_marks = sum(student_marks[query_name])/len(student_marks[query_name])       #O(m) + O(1)
    
print(f"{student_avg_marks:.2f}")


#Time complexity : O(n*m)
#Space complexity : O(n*m)