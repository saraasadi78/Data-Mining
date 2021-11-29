import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Walt_disney_movie_dataset.csv')
#sns.set(style="darkgrid")

running_time = df['Running time (int)']
budget = df['Budget (float)']
box_office = df['Box office (float)']

df['Running time (int)'].describe
plt.figure(figsize =(12,8))
plt.boxplot(running_time)
plt.title("Running time Boxplot")
plt.xlabel("Running time")
plt.ylabel("minute")
plt.grid(True)
plt.tight_layout()
plt.show()

df['Budget (float)'].describe
plt.figure(figsize =(12,8))
plt.boxplot(budget)
plt.title("Budget Boxplot")
plt.xlabel("Budget")
plt.grid(True)
plt.tight_layout()
plt.show()

df['Box office (float)'].describe
plt.figure(figsize =(12,8))
plt.boxplot(box_office)
plt.title("Box office Boxplot")
plt.xlabel("Box office")
plt.ylabel("million")
plt.grid(True)
plt.tight_layout()
plt.show()
