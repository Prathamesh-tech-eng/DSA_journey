'''Problem Statement : I am provided with a range, I need to find all fibonacci no. within given range, and print a list containing cubed 
                       fibonacci numbers
                       e.g : n = 4    O/P : [0, 1, 1, 8]
                       Link : https://www.hackerrank.com/challenges/map-and-lambda-expression
                       
Apprach : I will use map() to turn each fibonacci into cube. to find fibonacci, i am going to use three variable, a, b and c, and 
          initalize start with 0, 1
          '''


cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 0:
        return []
    lst = [0,1]
    a,b = 0,1
    for i in range(n-2): 
        c = a + b
        a = b
        b = c
        lst.append(c)
    return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#Time Complexity : O(n)
#Space Complexity : O(n)

#There is also more improved approach :

cube = lambda x: x**3

def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci_gen(n))))

#Sam Time and Space Complexity
