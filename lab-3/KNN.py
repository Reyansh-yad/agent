import numpy as np
from collections import Counter

# Step 1: Define distance function (Euclidean Distance)
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Step 2: Define KNN class
class KNN:
    def __init__(self, k=3):
        self.k = k
        
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        
    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions
    
    def _predict(self, x):
        # Compute distances
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        
        # Get k nearest samples
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # Majority vote
        most_common = Counter(k_nearest_labels).most_common()
        return int(most_common[0][0])

# Example Dataset
X_train = np.array([[1,2], [2,3], [3,3], [6,5], [7,7], [8,6]])
y_train = np.array([0,0,0,1,1,1])

# Create model
model = KNN(k=3)
model.fit(X_train, y_train)

# Predict new data
X_test = np.array([[5,5]])
prediction = model.predict(X_test)

print("Prediction:", prediction)
