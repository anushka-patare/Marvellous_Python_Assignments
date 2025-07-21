import numpy as np
import pandas as pd

def main():
    data = {'Grade':['A+','B','A','C','B+']}

    df = pd.DataFrame(data)
    
    new_data = {'A+':'Excellent','B':'Very Good','A':'Good','C':'Average','B+':'Poor'}

    df['Grade'] = df['Grade'].replace(new_data)
    print(df)


if __name__=="__main__":
    main()