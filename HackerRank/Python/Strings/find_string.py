'''Problem Discription : I am provided a string and a substring, if substring is present in the string, i need to print the occurence
                         e.g : str1 : PRATHATHA  str2 : ATHA        O/P : 2
                         Link : https://www.hackerrank.com/challenges/find-a-string
                         
Approach : could have used .count(), but it will miss the overlapping part, so I will use for loop , and 
           total iteration will be len(string) - len(substring) + 1, and I will check presence of substring after each iterations'''

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):      #O(n - m + 1)
        if string[i: i + len(sub_string)] == sub_string:     #string[i:i+len(sub_string)] = O(m)
            count += 1
        
    return count

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)

#Time complexity : O(n * m)