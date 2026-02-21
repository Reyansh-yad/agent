import numpy as np

# Example patterns (bipolar form)
X = np.array([[1, -1, 1]])      # ID
Y = np.array([[1, 1, -1]])      # Phone

# Weight matrix
W = X.T @ Y

print("Weight Matrix:\n", W)

# Recall
def recall_x_to_y(x):
    y = np.sign(x @ W)
    return y

def recall_y_to_x(y):
    x = np.sign(y @ W.T)
    return x

print("Recall Phone from ID:", recall_x_to_y(X))
print("Recall ID from Phone:", recall_y_to_x(Y))
