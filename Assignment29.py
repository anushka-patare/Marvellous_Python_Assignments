import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score,ConfusionMatrixDisplay

def Diabetes(Datapath):
    df = pd.read_csv(Datapath)
    
    print(df.head())
    print(df.info())
    print(df.isnull())
    print(df.describe())
    
    plt.hist(df['Outcome'],bins = 10 , color ="skyblue",edgecolor="black")
    plt.xlabel("Outcome")
    plt.ylabel("Frequency")
    plt.title(" Histogram for diabetes ")
    plt.show()
     
    sns.pairplot(df,hue="Outcome")
    plt.show()

    columns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
    print(df.columns==0)
    df[columns] = df[columns].replace(0,np.nan)
    print(df)
    df[columns]=df[columns].fillna(df[columns].mean())

    scaler = StandardScaler()
    print(scaler.fit_transform(df))

    X = df.drop(columns = ['Outcome'])
    Y = df['Outcome']

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = LogisticRegression()
    model.fit(X_train,Y_train)
    y_pred =model.predict(X_test)
    accuracy = accuracy_score(Y_test,y_pred)
    print("Accuracy by using logisticregression :",accuracy)
    cm1 = confusion_matrix(Y_test,y_pred)
    print("Confusion matrix by using Logisticregression",cm1)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,Y_train)
    y_pred =model.predict(X_test)
    accuracy = accuracy_score(Y_test,y_pred)
    print("Accuracy by using Kneighborsclassifier :",accuracy)
    cm2 = confusion_matrix(Y_test,y_pred)
    print("Confusion matrix by using KNeighborsclassifier:",cm2)

    precision = precision_score(Y_test,y_pred)
    print("Precision is :",precision)

    recall = recall_score(Y_test,y_pred)
    print("Recall is:",recall)

    f1score = f1_score(Y_test,y_pred)
    print("f1 score is:",f1score)
     
    con_mat = ConfusionMatrixDisplay(confusion_matrix=cm1)
    con_mat.plot(cmap = plt.cm.Blues)
    plt.title("Confusion matrix")
    plt.show()
    
    con_mat = ConfusionMatrixDisplay(confusion_matrix=cm2)
    con_mat.plot(cmap = plt.cm.Blues)
    plt.title("Confusion matrix")
    plt.show()

    print("Result is:",model.predict([[3,126,88,41,235,39.3,0.704,27],[7,147,76,0,0,39.4,0.257,43]]))
    df.to_csv("DiabetiesDetails.csv",index=False)

def main():
    Diabetes("diabetes.csv")

if __name__=="__main__":
    main()