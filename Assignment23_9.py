import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def main():
   
    data2 = {'Name':['Amit','Sagar','Pooja'],
             'Math':[np.nan,76,88],
             'Science':[91,np.nan,85]}
    
    df = pd.DataFrame(data2)
    
    print("dataFrame before null values:")
    print(df)

    df.fillna(df.mean(numeric_only = True),inplace = True)
    print("DataFrame after filling null values")
    print(df)


    """ null_values1=df['Math'].fillna(df['Math'].mean())
    print(null_values1)

    null_value2=df['Science'].fillna(df['Science'].mean())
    print(null_value2)"""

if __name__=="__main__":
    main()