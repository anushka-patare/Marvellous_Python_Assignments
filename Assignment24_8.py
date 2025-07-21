#Plot a histogram of math marks

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
    
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(8,5))
    plt.hist(df['Math'],bins=10,color="Skyblue",edgecolor='black')
    plt.xlabel("Marks")
    plt.ylabel("Range")
    plt.title("Histogram for maths marks")
    plt.show()
    
if __name__=="__main__":
    main()
    