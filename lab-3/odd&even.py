import numpy as np

# Training data (last bit determines odd/even)
# 0 = Even, 1 = Odd
X = np.array([[0], [1]])     # Input (last binary digit)
y = np.array([1, -1])        # Even=1, Odd=-1

# Initialize
w = np.random.randn(1)
b = np.random.randn()
learning_rate = 0.1

# Training
for epoch in range(10):
    for i in range(len(X)):
        output = np.sign(np.dot(w, X[i]) + b)
        if output != y[i]:
            w += learning_rate * y[i] * X[i]
            b += learning_rate * y[i]

print("Trained weight:", w)
print("Trained bias:", b)

# Testing
num = int(input("Enter number: "))
test = num % 2
result = np.sign(np.dot(w, test) + b)

if result == 1:
    print("Even Number")
else:
    print("Odd Number")
