import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('Walt_disney_movie_dataset.csv')

# plt.scatter(df['Running time (int)'],df['Budget (float)'])
# plt.show()
Time_Budget = df[['Running time (int)', 'Budget (float)']]
Time_Budget=Time_Budget.fillna(0)

#Normalize the values
X = StandardScaler().fit_transform(Time_Budget)

epsilon=0.25
db = DBSCAN(eps=epsilon).fit(Time_Budget)
db.fit(X)

y_pred = db.fit_predict(X)
plt.figure(figsize=(10,6))
plt.scatter(X[:,0], X[:,1],c=y_pred, cmap='Paired')
plt.title("Clusters determined by DBSCAN")
plt.show()

print(db.labels_)
df['cluster']=db.labels_
df.groupby(by=['cluster']).first
print(df)
