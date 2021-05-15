from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
import time
from sklearn.model_selection import train_test_split
import pandas as pd
import io
from sklearn.preprocessing import LabelEncoder
from category_encoders import TargetEncoder

d = pd.read_csv("disease.csv")
d.head()
d['disease'].unique()
d1 = d.iloc[:, 1:]
d1
labelencoder = LabelEncoder()
# Assigning numerical values and storing in another column
d1['disease'] = labelencoder.fit_transform(d1['disease'])
d1
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
d1['angry'] = encoder.fit_transform(d1['angry'], d1['disease'])
encoder = TargetEncoder()
d1['dull'] = encoder.fit_transform(d1['dull'], d1['disease'])
encoder = TargetEncoder()
d1['tearfull'] = encoder.fit_transform(d1['tearfull'], d1['disease'])
encoder = TargetEncoder()
d1['distracted'] = encoder.fit_transform(d1['distracted'], d1['disease'])
encoder = TargetEncoder()
d1['social'] = encoder.fit_transform(d1['social'], d1['disease'])
encoder = TargetEncoder()
d1['hyper'] = encoder.fit_transform(d1['hyper'], d1['disease'])

d2 = d1
d2


x = d2.iloc[:, :-1].values
y = d2.iloc[:, -1].values
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=0)
start = time.time()
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(x_train, y_train)
end = time.time()
print(end - start, "seconds")
