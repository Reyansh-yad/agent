import numpy as np

# Step 1: Initialize K-Means Class
class KMeans:
    def __init__(self, k=2, max_iters=100):
        self.k = k
        self.max_iters = max_iters

    def fit(self, X):
        self.X = X
        
        # Step 2: Initialize centroids (first k points)
        self.centroids = X[:self.k]

        for _ in range(self.max_iters):
            # Step 3: Assign clusters
            self.labels = self._assign_clusters()

            # Step 4: Calculate new centroids
            new_centroids = np.array([
                self.X[self.labels == i].mean(axis=0)
                for i in range(self.k)
            ])

            # Step 5: Check convergence
            if np.all(self.centroids == new_centroids):
                break

            self.centroids = new_centroids

    def _assign_clusters(self):
        distances = np.sqrt(((self.X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)

    def predict(self, X):
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)


#  Dataset
X = np.array([[1,2], [2,3], [3,3], [6,5], [7,7], [8,6]])

# Create Model
model = KMeans(k=2)
model.fit(X)

print("Centroids:")
print(model.centroids)

print("Cluster Labels:")
print(model.labels)
