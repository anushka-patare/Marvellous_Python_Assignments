#Normalize the Math scores using MinMax scaling.MinMaxScaler

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def main():
    line = "*"*70
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    df = pd.DataFrame(data)
    
    scaler = MinMaxScaler()
    print("dataframe before normalization:")
    print(df)
    
    print(line)

    df['Math']=scaler.fit_transform(df[['Math']])
    print("Dataframe after normalization :")
    print(df)

if __name__=="__main__":
    main()

  