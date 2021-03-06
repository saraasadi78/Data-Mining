import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn import metrics
from sklearn.metrics import cluster
import statistics
from sklearn.metrics import silhouette_score
from sklearn.metrics import adjusted_rand_score

df = pd.read_csv('Walt_disney_movie_dataset.csv')

# plt.scatter(df['Running time (int)'],df['Budget (float)'])
# plt.show()
Time_Budget = df[['Running time (int)', 'Budget (float)']]
Time_Budget=Time_Budget.fillna(0)

#Choosing the Appropriate Number of Clusters
kmeans_kwargs = {
"init": "random",
"n_init": 10,
"max_iter": 300,
"random_state": 42,
}
 
sse = []
for k in range(1, 15):
    modele = KMeans(n_clusters=k, **kmeans_kwargs)
    modele.fit(Time_Budget)
    sse.append(modele.inertia_)


plt.plot(range(1, 15), sse)
plt.xticks(range(1, 15))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()


silhouette_coefficients = []
for k in range(8, 15):
    modele = KMeans(n_clusters=k, **kmeans_kwargs)
    modele.fit(Time_Budget)
    score = silhouette_score(Time_Budget, modele.labels_)
    silhouette_coefficients.append(score)

plt.plot(range(8, 15), silhouette_coefficients)
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Coefficient")
plt.show()

#so the best number of clusters is 14


k_mean=KMeans(n_clusters=14, n_init=10, max_iter=300, tol=1e-4, verbose=0, random_state=None, copy_x=True, algorithm="auto")
k_mean.fit(Time_Budget)

identified_clusters = k_mean.fit_predict(Time_Budget)
data_with_clusters = df.copy()
data_with_clusters['Clusters'] = identified_clusters
plt.scatter(data_with_clusters['Running time (int)'],data_with_clusters['Budget (float)'],c=data_with_clusters['Clusters'],cmap='rainbow')
plt.title("K-MEANS (K=8)")
plt.show()

print(k_mean.labels_)
df['cluster']=k_mean.labels_
print(df)

df.groupby(by=['cluster']).first
#our data is successfully clustered


print("ARI=", adjusted_rand_score())


###############################################################################
#clustering by writer and directors:

# d=df['Directed by']
# w=df['Written by']
#
#
# def nominal2numeric(nominal):
#     numeric_value =1
#     nominal_uq_map = {}
#     numeric_ret_list =[]
#     for i in nominal:
#         if i in nominal_uq_map:
#             numeric_ret_list.append(nominal_uq_map[i])
#         else:
#             nominal_uq_map[i] = numeric_value
#             numeric_value += 1
#             numeric_ret_list.append(nominal_uq_map[i])
#     return pd.DataFrame(numeric_ret_list)
#
#
# director = nominal2numeric(d)
# writer = nominal2numeric(w)
#
# director.columns = ['Director']
# writer.columns = ['Writer']
#
# data = pd.concat([director, writer],axis=1)
#
# kmeans=KMeans(n_clusters=8,n_init=10,max_iter=300,tol=1e-4,verbose=0,random_state=None,copy_x=True,algorithm="auto")
# kmeans.fit(data)
#
# identified_clusters = kmeans.fit_predict(data)
# data_with_clusters = df.copy()
# data_with_clusters['Clusters'] = identified_clusters
# plt.scatter(data_with_clusters['Running time (int)'],data_with_clusters['Budget (float)'],c=data_with_clusters['Clusters'],cmap='rainbow')
# plt.show()

