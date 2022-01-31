import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt

df = pd.read_csv('Walt_disney_movie_dataset.csv')

df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values
df_non_numeric = df.select_dtypes(exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values

percentage_list = list()
cols_list = list()
for col in df.columns:
    missing_percentage = np.mean(df[col].isnull()) * 100
    cols_list.append(col)
    percentage_list.append(missing_percentage)

missing_percentage_DataFrame = pd.DataFrame()
missing_percentage_DataFrame['col'] = cols_list
missing_percentage_DataFrame['percentage_of_missing'] = percentage_list

missing_percentage_DataFrame.loc[missing_percentage_DataFrame.percentage_of_missing > 0].plot(kind='bar',
                                                                                              figsize=(12, 8))
# plt.show()

less_missing_values_cols_list = list(
    missing_percentage_DataFrame.loc[(missing_percentage_DataFrame.percentage_of_missing < 0.5)
                                     & (missing_percentage_DataFrame.percentage_of_missing > 0), 'col'].values)
df.dropna(subset=less_missing_values_cols_list, inplace=True)

# dropping columns with more than 40% null values
_40_pct_missing_cols_list = list(
    missing_percentage_DataFrame.loc[missing_percentage_DataFrame.percentage_of_missing > 40, 'col'].values)
df.drop(columns=_40_pct_missing_cols_list, inplace=True)

df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values
for col in numeric_cols:
    missing = df[col].isnull()
    num_missing = np.sum(missing)
    if num_missing > 0:
        med = df[col].median()  # impute with the median
        df[col] = df[col].fillna(med)

# zero means that there are no missing values left in our dataset now
# df.isnull().sum().sum()

#print(df["Running time (int)"].describe())
df = df.loc[df["Running time (int)"] > 20]
#print(df["Running time (int)"].describe())
#print(df.duplicated(subset=None, keep='first'))
df.drop_duplicates()


#Normalization with min_max for Running time and Budget columns with sklearn

from sklearn import preprocessing

std_scale = preprocessing.StandardScaler().fit(df[['Running time (int)', 'Budget (float)']])
df_std = std_scale.transform(df[['Running time (int)', 'Budget (float)']])

minmax_scale = preprocessing.MinMaxScaler().fit(df[['Running time (int)', 'Budget (float)']])
df_minmax = minmax_scale.transform(df[['Running time (int)', 'Budget (float)']])

print('\nStandard deviation after standardization:\n Running time={:.2f}, Budget={:.2f}'
      .format(df_std[:,0].std(), df_std[:,1].std()))

print('\nMin-value after min-max scaling:\n Running time={:.2f}, Budget={:.2f}'
      .format(df_minmax[:,0].min(), df_minmax[:,1].min()))
print('\nMax-value after min-max scaling:\n Running time={:.2f}, Budget={:.2f}'
      .format(df_minmax[:,0].max(), df_minmax[:,1].max()))

print(df['Running time (int)'])
print(df_std)

plt.figure(figsize=(8,6))
plt.scatter(df['Running time (int)'], df['Budget (float)'],color='green', label='input scale', alpha=0.5)
plt.scatter(df_std[:,0], df_std[:,1], color='red',label='Standardized', alpha=0.5)
plt.scatter(df_minmax[:,0], df_minmax[:,1],color='blue', label='min-max scaled [min=0, max=1]', alpha=0.5)

plt.title('scatter plot')
plt.xlabel('Running time (int)')
plt.ylabel('Budget (float)')
plt.legend(loc='upper left')
plt.grid()
plt.tight_layout()
plt.show()
