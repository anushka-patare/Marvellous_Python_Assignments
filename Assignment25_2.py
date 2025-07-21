import numpy as np
import pandas as pd

def main():

    data = {'Name':['A','B','C'],'Age':[21.0,22.0,23.0]}

    df = pd.DataFrame(data)

    print("Datatypes of columns are")
    print(df.dtypes)

    df['Age'] = df['Age'].astype(int)
    print(df['Age'])

if __name__=="__main__":
    main()