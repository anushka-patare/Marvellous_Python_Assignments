#Plot a pie chart of subject marks for sagar

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
    
    data1=['Math','Science','English']
    data2=[90,88,85]
    plt.figure(figsize=(8,5))
    plt.pie(data2,labels=data1,autopct='%1.1f%%')
    plt.title("All subjects marks of sagar")
    plt.show()
    
    print(line)
if __name__=="__main__":
    main()
