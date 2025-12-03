'''Problem Description : I am provided n → number of 1D arrays inside a 2D list (so you'll create n empty lists) q → number 
                         of queries to process A value lastAnswer, initialized to 0
                         There are two types of queries:

                        Type 1  : 1 x y . Find index: idx = (x ^ lastAnswer) % n
                                Append y to arr[idx]

                        Type 2  : 2 x y . Find index: idx = (x ^ lastAnswer) % n
                                Get element: lastAnswer = arr[idx][y % len(arr[idx])]
                                Store lastAnswer in a result array
                                
                        my task is to return result of every tupe 2 querry.
                        
                        Link : https://www.hackerrank.com/challenges/dynamic-array
                        
                        
Approach : '''