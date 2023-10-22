# -*- coding: utf-8 -*-
"""
Created on Tue Aug 1 14:00:54 2023
@author: erdem
"""

#%% Data Import (Data is available within the Sklearn library)
from sklearn.datasets import load_iris  # Data contents are predefined within the Sklearn library, and you can inspect the data's information from the DESCR attribute, feature details from Feature_names, and class details from the target.
import pandas as pd

#%% Data Frame Preparation
iris = load_iris()

data = iris.data
feature_names = iris.feature_names
y = iris.target

df = pd.DataFrame(data, columns=feature_names)
df["class"] = y  # Adding the class labels to the DataFrame

x = data

#%% PCA Objective: Reduce 4-dimensional data to 2 dimensions
from sklearn.decomposition import PCA

pca = PCA(n_components=2, whiten=True)  # n_components specifies how many dimensions we want to reduce the data to, and whiten=True normalizes the data. This is important because if one feature dominates the others, PCA can be biased towards it, so normalization is necessary.
pca.fit(x)  # Fit the PCA model to the data (y is not required for PCA)
x_pca = pca.transform(x)  # Transform the data using the constructed PCA model
print("Variance ratio:", pca.explained_variance_ratio_)  # Shows the variance explained by each component. The first component explains 92.46%, and the second component explains 5.30% of the variance.
print("Sum:", sum(pca.explained_variance_ratio_))  # Indicates that 97.76% of the variance is preserved, implying a successful PCA with a 2.24% data loss.

#%% 2D Plot
df["p1"] = x_pca[:, 0]
df["p2"] = x_pca[:, 1]
colors = ["red", "green", "blue"]
import matplotlib.pyplot as plt

for each in range(3):
    plt.scatter(df.p1[df["class"] == each], df.p2[df["class"] == each], color=colors[each], label=iris.target_names[each])
    # First, plot p1 and p2 for class 0 in red with label "setosa", then for class 1 in green with label "versicolor", and finally for class 2 in blue with label "virginica".
    
plt.legend()
plt.xlabel("p1")
plt.ylabel("p2")
plt.show()
