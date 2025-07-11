'''Problem Discription : I am provided a number, and I have to print the decimal value, binary value, hexadecimal value and Octal value
                         of each in range 1 to number. The printed o/p should be in a specific format, like each column is left padded
                         link : https://www.hackerrank.com/challenges/python-string-formatting
                         
Approach : I will use the built in functions like bin() oct() and hex() for the values and will use rjust to obtain the specified
           print format of left padding'''

def print_formatted(number):
    # your code goes here
    x = len(str(bin(number)))-2
    for i in range(1, number + 1):            #O(nlogn)
        dec = str(i).rjust(x)
        octal = oct(i)[2:].rjust(x)
        hexa = hex(i)[2:].upper().rjust(x)
        binary = bin(i)[2:].rjust(x)
        print(f"{dec} {octal} {hexa} {binary}")


n = int(input())
print_formatted(n)

#Time Complexity : O(nlogn)
#Space Complexity : O(n)