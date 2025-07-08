'''Problem Description : I am provide names and scores of student and I am supposed to provide list of names of student who 
                         obtained second-lowest scores, each name at new line.
                         eg. ravi = 30, gita = 20, tina = 25, jay = 25    o/p : jay, tina
                         link : https://www.hackerrank.com/challenges/nested-list

Approach : I am thinking of creating a dictionary with key == name and value == score, and then I will create a list of unique scores
           , we will sort that list, obtain the second lowest score, and then we will get all the names having value == second-lowest-score
           and then we will sort those name alphabetically and print them.'''

students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])

unique_score = sorted({score for name,score in students})  #O(nlogn)

second_lowest = unique_score[1]

names = [name for name , score in students if score == second_lowest]  #O(n)

for name in sorted(names):     #O(klogk)
    print(name)

#Time complexity : worst case scenario O(nlogn)

#but if I find the second-lowest score manually rather than applying sorted(), I can achieve even less time complexity

students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

first, second = int('inf')

for _,score in students :
    if score < first : 
        second = first
        first = score
    elif first < score < second :
        second = score

second_lowest = second

names = [name for name , score in students if score == second_lowest]  #O(n)

for name in sorted(names):     #O(klogk)
    print(name)
