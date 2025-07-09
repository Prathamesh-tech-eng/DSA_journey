'''Problem Description : I am provided a list eg. I am prathamesh, and I am supposed to split it, ["I", "am", "prathamesh"], and
                         print the sentence in format : I-am-prathamesh
                         Link : https://www.hackerrank.com/challenges/python-string-split-and-join
                         
Approach : I will create a function, and will use built in like split() and join()'''

def split_and_join(line):
    lst = line.split()            #O(n)
    lst = "-".join(lst)           #O(n)
    return lst


line = input()
result = split_and_join(line)
print(result)


#Time Complexity : O(n)