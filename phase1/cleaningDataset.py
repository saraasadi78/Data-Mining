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

print(df["Running time (int)"].describe())
df = df.loc[df["Running time (int)"] > 20]
print(df["Running time (int)"].describe())

print(df.duplicated(subset=None, keep='first'))
df.drop_duplicates()

print(df.columns)
df.drop(columns=['Running time','Box office (float)'],axis=1,inplace=True)
print(df.shape)
df.drop(['Budget','Release date (datetime)'],axis=1,inplace=True)
#print(df.shape): [450 rows x 17 columns]





