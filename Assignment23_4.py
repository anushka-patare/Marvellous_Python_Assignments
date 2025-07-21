#Display students who scored more than 85 in science

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

    print(line)
    print("Students who scored more than 85 marks in science is :")

    Name_of_students = df[df['Science']>85]
    print(Name_of_students)

    
if __name__=="__main__":
    main()