from sklearn.metrics import accuracy_score, precision_score, recall_score
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from category_encoders import TargetEncoder
import pandas as pd
import io
d = pd.read_excel(io.BytesIO(uploaded['major1500.xlsx']))
d.head()
d['result'].unique()
d1 = d.iloc[:, 1:]
d1
labelencoder = LabelEncoder()
# Assigning numerical values and storing in another column
d1['result'] = labelencoder.fit_transform(d1['result'])
d1
encoder = TargetEncoder()
d1['asleep'] = encoder.fit_transform(d1['asleep'], d1['result'])
encoder = TargetEncoder()
d1['depress'] = encoder.fit_transform(d1['depress'], d1['result'])
encoder = TargetEncoder()
d1['concentration'] = encoder.fit_transform(d1['concentration'], d1['result'])

encoder = TargetEncoder()
d1['academics'] = encoder.fit_transform(d1['academics'], d1['result'])
encoder = TargetEncoder()
d1['peergroup'] = encoder.fit_transform(d1['peergroup'], d1['result'])
encoder = TargetEncoder()
d1['socialmedia'] = encoder.fit_transform(d1['socialmedia'], d1['result'])
encoder = TargetEncoder()
d1['irritation'] = encoder.fit_transform(d1['irritation'], d1['result'])
encoder = TargetEncoder()
d1['afraid'] = encoder.fit_transform(d1['afraid'], d1['result'])
encoder = TargetEncoder()
d1['troublerelaxing'] = encoder.fit_transform(
    d1['troublerelaxing'], d1['result'])
encoder = TargetEncoder()
d1['controltemper'] = encoder.fit_transform(d1['controltemper'], d1['result'])
encoder = TargetEncoder()
d1['alone'] = encoder.fit_transform(d1['alone'], d1['result'])
encoder = TargetEncoder()
d1['anxiety'] = encoder.fit_transform(d1['anxiety'], d1['result'])
encoder = TargetEncoder()
d1['dead'] = encoder.fit_transform(d1['dead'], d1['result'])
x = d2.iloc[:, :-1].values
y = d2.iloc[:, -1].values
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=0)
# Decision Tree Classification
classifier = DecisionTreeClassifier(
    criterion='entropy', random_state=0, max_depth=8)
classifier.fit(x_train, y_train)
y3_pred = classifier.predict(x_test)
y8_pred = classifier.predict(x_train)
accuracy_score(y_test, y3_pred)
# accuracy_score(y_train,y8_pred)
#precision_score(y_train, y8_pred,average='weighted',labels=np.unique(y_pred))
#recall_score(y_train, y8_pred,average='weighted',labels=np.unique(y_pred))
