'''Problem Statement : I am provided with History scores and physics scores, I need to find the score of the regression line
                       # Slope of the Regression Line Formula (b1)

                        This formula calculates the slope of the least squares regression line.
                        The regression line is used to model the linear relationship between two variables,
                        typically an independent variable (X) and a dependent variable (Y).

                        Formula:
                        b1 = Σ[(xi - x_mean) * (yi - y_mean)] / Σ(xi - x_mean)²

                        Alternatively, using the covariance and variance:
                        b1 = Cov(X, Y) / Var(X)
                        
                        
                        Link : https://www.hackerrank.com/challenges/correlation-and-regression-lines-7
                        
'''

import numpy as np
import pandas as pd

PS = list(map(int, input().split()))
HS = list(map(int, input().split()))

Data = {
    'X' : PS,
    'Y' : HS
}

df = pd.DataFrame(Data)
X = np.array(df['X'].values)
Y = np.array(df['Y'].values)

X_mean = np.mean(X)
Y_mean = np.mean(Y)

numerator = np.sum((X - X_mean)*(Y - Y_mean))
denominator = np.sum((X - X_mean)**2)

slope = numerator/denominator

print(f"The Slope of the regression line is : {slope:.3f}")


#Time Complexity : O(n)
#Space Complexity : O(n)