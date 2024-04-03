# -*- coding: utf-8 -*-
"""LVADSUSR78_BPA_final-Q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/195uN5r4sQBbxXphRyLFLWaUONqfXrcM9
"""

# Commented out IPython magic to ensure Python compatibility.
#3
import warnings
warnings.filterwarnings("ignore")
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import seaborn as sns
# %matplotlib inline


df = pd.read_csv("/content/sample_data/seeds.csv")
print(df.head())

df = df.fillna(method='ffill')

#visualize correl
correl = df.corr()
print(correl)
sns.heatmap(correl, annot=True, fmt = '0.2f')

# Area feature outliers
plt.boxplot(df['Area'])
plt.show()

# Perimeter Feature outliers
plt.boxplot(df['Perimeter'])
plt.show()

# MinMax Scaler , normalizing features
minmax = MinMaxScaler()
minmax.fit(df[['Area']])
df['Area'] = minmax.transform(df[['Area']])
minmax.fit(df[['Perimeter']])
df['Perimeter']=minmax.transform(df[['Perimeter']])

# finding sum of squared error
sse = []
k_range = range(1,10)
for k in k_range:
   km = KMeans(n_clusters=k)
   km.fit(df)
   sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_range,sse)

# Building model

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df)
y_predicted
df['cluster']=y_predicted
print(km.cluster_centers_) # cluster centers

# Cluster visualization
df1 = df[df.cluster==0]
print(df1)
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.cluster,df1['Area'],color='green')
plt.scatter(df2.cluster,df2['Area'],color='red')
plt.scatter(df3.cluster,df3['Area'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Cluster')
plt.ylabel('Area')
plt.legend()