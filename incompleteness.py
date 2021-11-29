#finf and visualize percentage of Missing Values in each column
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Walt_disney_movie_dataset.csv')

df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values
df_non_numeric = df.select_dtypes(exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values

percentage_list = list()
cols_list = list()
names=list()

for col in df.columns:
    missing_percentage = np.mean(df[col].isnull()) * 100
    cols_list.append(col)
    percentage_list.append(missing_percentage)
    names.append(col)

plt.figure(figsize=(16,12), dpi= 90)
plt.barh(names,percentage_list, color='#87CEFA')
plt.xlabel("percentage of missing values")
plt.title('Bar plot for missing information of each column')
plt.grid(linestyle='--', alpha=0.5)
plt.show()







