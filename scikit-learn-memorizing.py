import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = np.loadtxt('old_faithful_geyser.csv',skiprows=1,delimiter=",")

X = data

kmeans = KMeans(n_clusters=2,random_state=0)
kmeans.fit(X)

labels = KMeans.labels_
centroids = KMeans.cluster_centers_

print()