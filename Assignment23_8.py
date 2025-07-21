#Plot a line chart of marks for Amit across all subjects.and

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

    all_subjects = ['Math','Science','English']
    all_marks=[85,92,75]
    plt.figure(figsize=(8,5))
    plt.plot(all_subjects,all_marks)
    plt.title("Bar plot of amits marks")
    plt.xlabel(" all Subjects")
    plt.ylabel("all marks")
    plt.show()
    
if __name__=="__main__":
    main()