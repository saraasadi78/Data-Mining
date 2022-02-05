import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

df = pd.read_csv('Walt_disney_movie_dataset.csv')

df['Box office (float)'] = df['Box office (float)'].replace(np.NaN, 0)
df['Budget (float)'] = df['Budget (float)'].replace(np.NaN, 0)

df['profit'] = df.apply(lambda _: '', axis=1)

df = df.reset_index()
for index, row in df.iterrows():
    df['profit'] = df['Box office (float)'] - df['Budget (float)']

df['profit'].apply(np.ceil)
df['profit'].round(decimals = 3)

df['Class'] = df.apply(lambda _: '', axis=1)

df['profit']=df['profit'].astype(np.int64)

for index, row in df.iterrows():
    if df['profit'].ge(0).all():
        df['Class']="Bestselling movie"
    else:
        df['Class']="Low-selling movie"

x = df.iloc[:, :-1].values
y = df.iloc[:, 12].values

x_train, x_test, y_train, y_test = train_test_split(x, df['Class'], test_size=0.4)

clf = svm.SVC(kernel='linear',c=1, gamma=1)

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#96.49%, considered as very good accuracy :)

print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))
