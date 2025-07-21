#Create a bar plot of stdents names vs total marks

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def main():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    df = pd.DataFrame(data)
    
    df['Total']=df[['Math','Science','English']].sum(axis='columns')
    print("Total marks are:",df)

    plt.figure(figsize=(8,5))
    sns.barplot(x='Name',y='Total',data=df)
    plt.xlabel("Students name")
    plt.ylabel("Toal marks")
    plt.title("Bar plot according to students names and total marks")
    plt.show()
    
if __name__=="__main__":
    main()