import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.cluster import KMeans, AgglomerativeClustering


def generate_data(n_samples, flagc):
    # 3 grupe
    if flagc == 1:
        random_state = 365
        X, y = make_blobs(n_samples=n_samples, random_state=random_state)

    # 3 grupe
    elif flagc == 2:
        random_state = 148
        X, y = make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)

    # 4 grupe
    elif flagc == 3:
        random_state = 148
        X, y = make_blobs(
            n_samples=n_samples,
            centers=4,
            cluster_std=np.array([1.0, 2.5, 0.5, 3.0]),
            random_state=random_state,
        )
    # 2 grupe
    elif flagc == 4:
        X, y = make_circles(n_samples=n_samples, factor=0.5, noise=0.05)

    # 2 grupe
    elif flagc == 5:
        X, y = make_moons(n_samples=n_samples, noise=0.05)

    else:
        X = []

    return X


# generiranje podatkovnih primjera
X = generate_data(500, 1)

# prikazi primjere u obliku dijagrama rasprsenja
plt.figure()
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.title("podatkovni primjeri")
plt.show()


# 1.2
# Primijenite metodu K srednjih vrijednosti te ponovo prikažite primjere, ali svaki primjer
# obojite ovisno o njegovoj pripadnosti pojedinoj grupi. Nekoliko puta pokrenite programski
# kod. Mijenjate broj K. Što primjecujete?
km = KMeans(n_clusters=5)
km.fit(X)
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=km.labels_)
labels = km.predict(X)
centers = km.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c="black", s=100, alpha=0.8)
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.title("podatkovni primjeri")
plt.show()

# 1.3
