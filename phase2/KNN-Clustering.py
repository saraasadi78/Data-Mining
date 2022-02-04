import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

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

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)
pred = classifier.predict(x_test)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

error = []
# Calculating error for K values between 1 and 40
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train, y_train)
    pred_i = knn.predict(x_test)
    error.append(np.mean(pred_i != y_test))


plt.figure(figsize=(12, 6))
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')

