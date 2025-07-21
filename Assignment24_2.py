#Create a gender column and perform one-hot encoding

import pandas as pd
import numpy as np

def main():
    line="*"*65
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    df = pd.DataFrame(data)

    df['Gender'] = ['Male','Male','Female']
    print(df)
    encode=pd.get_dummies(df[['Gender']])
    print(encode)
    

    

if __name__=="__main__":
    main()
