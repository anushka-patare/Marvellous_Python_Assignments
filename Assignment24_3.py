#Group  students by gender and calculate average marks.

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
    
    print(line)
    
    Marks=['Math','Science','English']
    group_students=df.groupby('Gender')[Marks].mean()
    print(group_students)

if __name__=="__main__":
    main()
