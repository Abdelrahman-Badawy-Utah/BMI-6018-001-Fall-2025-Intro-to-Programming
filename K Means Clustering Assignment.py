# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 14:40:21 2025

@author: El-Wattaneya
"""

# ---------------------------------------------------------------------
# I used the Diabetes dataset and I only included the numerical columns as it's compatible with K-means clustering
# 1. Importing needed libraries and Loading Dataset
# ---------------------------------------------------------------------
pip install kneed


import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from kneed import KneeLocator

df = pd.read_csv(r'C:\Users\El-Wattaneya\Desktop\Module 13 intro to programming\diabetic_data.csv')

# Selecting relevant numerical features
features = [
    'time_in_hospital', 'num_lab_procedures', 'num_procedures',
    'num_medications', 'number_outpatient', 'number_emergency',
    'number_inpatient', 'number_diagnoses'
]

# Creating a new dataframe X with the selected features
X = df[features]

# Checking for missing values (K-means cannot process NaN) - No missing valus in these features were found
X.isnull().sum()


# ---------------------------------------------------------------------
# 2. Standardizing Features using the StandardScaler method (required for K-means)
# ---------------------------------------------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---------------------------------------------------------------------
# 3. Computing the Sum of Squared Error SSE for k = 1 to 10  (Elbow Method)
# ---------------------------------------------------------------------
sse = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)

print("SSE for each k:", sse)

# ---------------------------------------------------------------------
# 4. Plotting the Elbow Curve
# ---------------------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(k_values, sse, marker='o')
plt.title("Elbow Method for Optimal Number of Clusters")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Sum of Squared Errors (SSE)")
plt.xticks(k_values)
plt.grid(True)
plt.savefig("elbow_curve.png")
plt.show()

# ---------------------------------------------------------------------
# 5. Automatically detecting the "Elbow" rather than visually using kneelocator
# ---------------------------------------------------------------------
knee = KneeLocator(k_values, sse, curve='convex', direction='decreasing')
optimal_k = knee.elbow if knee.elbow is not None else 3  # fallback = 3

print(f"Detected optimal number of clusters: k = {optimal_k}")

# ---------------------------------------------------------------------
# 6. Fitting Final K-Means Model Using Optimal k
# ---------------------------------------------------------------------
kmeans_opt = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
kmeans_opt.fit(X_scaled)

clusters = kmeans_opt.predict(X_scaled)
centroids = kmeans_opt.cluster_centers_

# ---------------------------------------------------------------------
# 7. Using PCA to Reduce Dimensions to 2D for Cluster Visualization
# ---------------------------------------------------------------------
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
centroids_pca = pca.transform(centroids)

# ---------------------------------------------------------------------
# 8. Plotting the Clusters and Centroids
# ---------------------------------------------------------------------
plt.figure(figsize=(10, 8))

# Plotting each cluster separately
for i in range(optimal_k):
    plt.scatter(
        X_pca[clusters == i, 0],
        X_pca[clusters == i, 1],
        s=15, alpha=0.6,
        label=f'Cluster {i + 1}'
    )

# Plotting centroids
plt.scatter(
    centroids_pca[:, 0], centroids_pca[:, 1],
    s=300, c='black', marker='X', label='Centroids'
)

plt.title(f'K-Means Clusters (k = {optimal_k}) Visualized with PCA')
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.grid(True)
plt.savefig("cluster_visualization.png")
plt.show()



