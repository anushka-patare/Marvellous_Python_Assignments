#Add a new column 'Total' to the DataFrame as the sum of all subject marks.TimeoutError

import pandas as pd
import numpy as np

def main():
    line = "*"*60
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    df = pd.DataFrame(data)
    
    print("DataFrame before Total column",df)

    df['Total']=df[['Math','Science','English']].sum(axis='columns')
    
    print(line)
    
    print("DataFrame after Total column",df)

if __name__=="__main__":
    main()