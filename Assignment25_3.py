import pandas as pd
import numpy as np

def main():
    data = {'City':['Pune','Mumbai','Delhi','Pune','Delhi']}

    df = pd.DataFrame(data)

    #Pune=1
    #Mumbai=2
    #Delhi=3

    df['City']=df['City'].map({'Pune':1,'Mumbai':2,'Delhi':3})
    print(df)

if __name__=="__main__":
    main()
