import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def WinePredictor(Datapath):
    df = pd.read_csv(Datapath)

    print(df.shape)
    print(df.head())
    
    df.dropna(inplace = True)

    x=df.drop(columns = ['Class'])
    y=df['Class']
    
    x_train , x_test ,y_train,y_test =train_test_split(x,y,test_size = 0.2,random_state=42)
    
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test,y_pred)
    print("Accuracy score is :",accuracy*100)

def main():
    WinePredictor("WinePredictor.csv")


if __name__=="__main__":
    main()