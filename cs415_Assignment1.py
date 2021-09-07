import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    
    # * Input the values for the dataframe
    df = pd.DataFrame({"A": [1,2,4,2,5,3,5,1,6,2],
                    "B": [100, 300, 200, 600, 100, 200, 300, 100, 400, 200],
                    "C": [10, 15, 20, 10, 30, 16, 25, 11, 25, 19]})

    # * Choose new values to compare against the dataframe 
    newValue = [4, 500, 40]

    # * Find the mean of each column
    mean = []
    [mean.append(np.mean(y)) for x,y in df.iteritems()]

    
    # * find the "distance" from the mean, or the (x-m)
    distance = [x - y for x,y in zip(newValue, mean)]
    
    # * find the inverse of the covariance of the matrix
    invcov = np.linalg.inv(df.cov())
    
    # * (x-m)^t * Σ^-1 * (x-m )----  calculating this part buy using the numpy dot product method
    MD_squared = np.dot(np.dot(distance,invcov),distance)
    
    # * Calculate Mahalanobis Distance by returning the squared root of the previous answer
    print(np.sqrt(MD_squared))
    
if __name__ == "__main__":
    main()