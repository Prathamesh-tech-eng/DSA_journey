'''Problem Description : I am provided Physics scores and history scores, I need to apply the pearson coorelation method and find the 
                         coorelation vales. 
                         # Pearson Correlation Coefficient Formula

                        This formula calculates the linear correlation between two sets of data.
                        It ranges from -1 to +1, where:
                        +1 indicates a perfect positive linear relationship
                        -1 indicates a perfect negative linear relationship
                         0 indicates no linear relationship

                        Formula:
                        r = Σ[(xi - x_mean) * (yi - y_mean)] / √[Σ(xi - x_mean)² * Σ(yi - y_mean)²]

                        Where:
                        r         = Pearson correlation coefficient
                        xi        = individual data point for variable X
                        x_mean    = mean of variable X
                        yi        = individual data point for variable Y
                        y_mean    = mean of variable Y
                        Σ         = summation (sum of all data points)
                        √         = square root

                        --- Example Python Implementation (for demonstration) --- 
                        
                        
                        Link : https://www.hackerrank.com/challenges/correlation-and-regression-lines-6
                        '''


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
import pandas as pd

PS = list(map(int, input().split()))
HS = list(map(int, input().split()))

data = {
    'PS' : PS,
    'HS' : HS
}

df = pd.DataFrame(data)

X = np.array(df['PS'].values)
Y = np.array(df['HS'].values)

X_mean = np.mean(X)
Y_mean = np.mean(Y)

numerator = np.sum((X - X_mean) * (Y - Y_mean))
denominator = np.sqrt((np.sum((X - X_mean)**2) * (np.sum((Y - Y_mean)**2))))

r = numerator/denominator




#The built in way : 
from scipy.stats import pearsonr
import math

built_in_r, _ = pearsonr(PS, HS)

print(f"Manual Pearson r: {r:.3f}")
print(f"Built-in Pearson r: {built_in_r:.3f}")

#Time Complexity : O(n)
#Space Complexity : O(n)
