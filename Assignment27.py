import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def Advertise(Datapath):
    df = pd.read_csv(Datapath)
    print(df)

    x = df.drop(columns = ['sales'])
    y = df['sales']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    model = LinearRegression()
    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)
    print("Predicted values :",y_pred)

    print("Expected value is:",y_test)


def main():
    Advertise("Advertising.csv")


if __name__=="__main__":
    main()