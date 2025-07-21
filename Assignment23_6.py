#Sort the DataFrame by Total marks in descending order

import pandas as pd
import numpy as np

def main():
    line="*"*70
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    df = pd.DataFrame(data)
    
    df['Total']=df[['Math','Science','English']].sum(axis='columns')
    print("Total marks are:",df)

    print("DataFrame before sorting:")
    print(df)

    sorted=df.sort_values(by='Total',ascending=False)

    print(line)
    
    print("DataFrame after sorting:")
    print(sorted)
    
if __name__=="__main__":
    main()