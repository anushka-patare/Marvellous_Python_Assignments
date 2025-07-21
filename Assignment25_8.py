import pandas as pd
import numpy as np

def main():
    data = {'Marks':[85,np.nan,90,np.nan,95]}

    df = pd.DataFrame(data)
     
    null_values=df['Marks'].interpolate()
    print(null_values)


if __name__=="__main__":
    main()

    