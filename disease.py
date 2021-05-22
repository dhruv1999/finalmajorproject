import pandas as pd
import numpy as np
import settings

a = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype='int')


def makePrediction2(a):

    d = pd.read_csv("disease.csv")

    from sklearn.model_selection import train_test_split
    from sklearn import preprocessing
    from sklearn.datasets import make_classification
    from sklearn.preprocessing import LabelEncoder
    from category_encoders import TargetEncoder

    from sklearn.tree import DecisionTreeClassifier

    from sklearn import metrics
    from sklearn.metrics import accuracy_score, mean_squared_error, precision_recall_curve
    from sklearn.model_selection import cross_val_score

    d1 = d.iloc[:, 1:]

    labelencoder = LabelEncoder()
    d1['disease'] = labelencoder.fit_transform(d1['disease'])
    print(d1)

    encoder = TargetEncoder()
    d1['talk'] = encoder.fit_transform(d1['talk'], d1['disease'])

    encoder = TargetEncoder()
    d1['active'] = encoder.fit_transform(d1['active'], d1['disease'])

    encoder = TargetEncoder()
    d1['highlow'] = encoder.fit_transform(d1['highlow'], d1['disease'])

    encoder = TargetEncoder()
    d1['selfconfidence'] = encoder.fit_transform(
        d1['selfconfidence'], d1['disease'])

    encoder = TargetEncoder()
    d1['work'] = encoder.fit_transform(d1['work'], d1['disease'])

    encoder = TargetEncoder()
    d1['dull'] = encoder.fit_transform(d1['dull'], d1['disease'])

    encoder = TargetEncoder()
    d1['angry'] = encoder.fit_transform(d1['angry'], d1['disease'])

    encoder = TargetEncoder()
    d1['tearfull'] = encoder.fit_transform(d1['tearfull'], d1['disease'])

    encoder = TargetEncoder()
    d1['distracted'] = encoder.fit_transform(d1['distracted'], d1['disease'])

    encoder = TargetEncoder()
    d1['social'] = encoder.fit_transform(d1['social'], d1['disease'])

    encoder = TargetEncoder()
    d1['hyper'] = encoder.fit_transform(d1['hyper'], d1['disease'])

    x = d1.iloc[:, :-1].values
    y = d1.iloc[:, -1].values

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=0)

    from sklearn.tree import DecisionTreeClassifier
    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier.fit(x_train, y_train)

    y3_pred = classifier.predict(x_test)
    print(y3_pred)
    from sklearn.metrics import accuracy_score
    print(accuracy_score(y_test, y3_pred))

    algo = DecisionTreeClassifier(criterion="entropy", randon_state=0)
    algo.fit(x_train, y_train)

    yp = algo.predict(a.reshape(1, -1))
    return yp
