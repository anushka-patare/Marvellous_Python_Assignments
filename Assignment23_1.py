import pandas as pd
import numpy as np

def main():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    df = pd.DataFrame(data)
    print("The shape of data is:",df.shape)
    print("The columns of dataframe is :",df.columns)
    print("The datatype is:",df.dtypes)


if __name__=="__main__":
    main()

