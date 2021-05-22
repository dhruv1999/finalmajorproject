from sklearn.metrics import accuracy_score, precision_score, recall_score
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from category_encoders import TargetEncoder
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import io
d = pd.read_excel(io.BytesIO(uploaded['Schizophrenia final.xlsx']))
d.head()
d['result'].unique()
d1 = d
d1
labelencoder = LabelEncoder()
# Assigning numerical values and storing in another column
d1['result'] = labelencoder.fit_transform(d1['result'])
encoder = TargetEncoder()
d1['control'] = encoder.fit_transform(d1['control'], d1['result'])
encoder = TargetEncoder()
d1['hear'] = encoder.fit_transform(d1['hear'], d1['result'])
encoder = TargetEncoder()
d1['difficult'] = encoder.fit_transform(d1['difficult'], d1['result'])
encoder = TargetEncoder()
d1['see'] = encoder.fit_transform(d1['see'], d1['result'])
encoder = TargetEncoder()
d1['struggle'] = encoder.fit_transform(d1['struggle'], d1['result'])
encoder = TargetEncoder()
d1['thinking'] = encoder.fit_transform(d1['thinking'], d1['result'])
encoder = TargetEncoder()
d1['tracked'] = encoder.fit_transform(d1['tracked'], d1['result'])
encoder = TargetEncoder()
d1['jealous'] = encoder.fit_transform(d1['jealous'], d1['result'])
encoder = TargetEncoder()
d1['person'] = encoder.fit_transform(d1['person'], d1['result'])
encoder = TargetEncoder()
d1['speaking'] = encoder.fit_transform(d1['speaking'], d1['result'])
encoder = TargetEncoder()
d1['medical'] = encoder.fit_transform(d1['medical'], d1['result'])
d2 = d1
d2
x = d2.iloc[:, :-1].values
y = d2.iloc[:, -1].values
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=0)
# Decision Tree Classification
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(x_train, y_train)
y3_pred = classifier.predict(x_test)
accuracy_score(y_test, y3_pred)
