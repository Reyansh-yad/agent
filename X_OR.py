import numpy as np

# XOR dataset
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

# Initialize weights
np.random.seed(42)
W1 = np.random.randn(2, 4)
W2 = np.random.randn(4, 1)

# Activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Training
for epoch in range(10000):
    # Forward pass
    hidden = sigmoid(np.dot(X, W1))
    output = sigmoid(np.dot(hidden, W2))

    # Backpropagation
    error = y - output
    d_output = error * sigmoid_derivative(output)
    d_hidden = d_output.dot(W2.T) * sigmoid_derivative(hidden)

    # Update weights
    W2 += hidden.T.dot(d_output) * 0.1
    W1 += X.T.dot(d_hidden) * 0.1

# Testing
print("Results for XOR Gate:")
for i in range(len(X)):
    hidden = sigmoid(np.dot(X[i], W1))
    output = sigmoid(np.dot(hidden, W2))
    print(f"Input: {X[i]} -> Prediction: {round(float(output[0]))}")
