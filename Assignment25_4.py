import pandas as pd 
import numpy as np

def main():

    data = {'Department':['HR','IT','Finance','HR','IT']}

    df = pd.DataFrame(data)

    encoded_data= pd.get_dummies(df['Department'])

    print(encoded_data)


if __name__=="__main__":
    main()