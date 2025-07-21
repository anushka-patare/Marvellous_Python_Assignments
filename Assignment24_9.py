#Rename 'Math' column to 'Mathematics'
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

    df.rename(columns={'Math':'Mathematics'},inplace=True)
    print(df)

if __name__=="__main__":
    main()
    