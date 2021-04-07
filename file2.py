import pandas as pd
import numpy as np
import settings

a = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype='int')


def makePrediction(a):
    


    mental_health_train = pd.read_csv("major.csv")

   
    from sklearn.model_selection import train_test_split
    from sklearn import preprocessing
    from sklearn.datasets import make_classification
    from sklearn.preprocessing import binarize, LabelEncoder, MinMaxScaler

   
    from sklearn.tree import DecisionTreeClassifier
   

   
    from sklearn import metrics
    from sklearn.metrics import accuracy_score, mean_squared_error, precision_recall_curve
    from sklearn.model_selection import cross_val_score


    mental_health_train.drop('Timestamp', axis=1, inplace=True)
    mental_health_train.drop('Age', axis=1, inplace=True)
    mental_health_train.shape


    labelDict = {}
    for feature in mental_health_train:
        le = preprocessing.LabelEncoder()
        le.fit(mental_health_train[feature])
        le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
        mental_health_train[feature] = le.transform(
            mental_health_train[feature])

        labelKey = 'label_' + feature
        labelValue = [*le_name_mapping]
        labelDict[labelKey] = labelValue

    mental_health_train

    x_train = mental_health_train.iloc[:, 0:12]
    y_train = mental_health_train.iloc[:, 12:13]
    
    algo=DecisionTreeClassifier(criterion="entropy",randon_state=0)
    algo.fit(x_train, y_train)

    yp = algo.predict(a.reshape(1, -1))
    return yp


