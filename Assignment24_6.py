#Count how many students passed.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    line="*"*50
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    print(line)
    df = pd.DataFrame(data)
    
    df['Total']=df[['Math','Science','English']].sum(axis='columns')
    print("Total marks are:",df)
    
    print(line)
    df['Status'] = df['Total'].apply(lambda x : 'Pass' if x>250 else 'Fail' )
    print(df)
    
    print(line)
    count = (df['Status'].value_counts()['Pass'])
    print(count)

if __name__=="__main__":
    main()