#Replace 'Pooja' with 'Puja' in the "name' Column

import pandas as pd
import numpy as np

def main():
    line = "*"*70
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    df = pd.DataFrame(data)
    
    print("DataFrame before replacement:")
    print(df)

    df['Name']=df['Name'].replace('Pooja','Puja')

    print(line)

    print("DataFrame after replacement:")
    print(df)
     

    
if __name__=="__main__":
    main()