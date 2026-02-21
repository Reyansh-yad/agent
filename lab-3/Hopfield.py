import numpy as np

# Stored pattern (bipolar)
pattern = np.array([1, -1, 1, -1])

# Weight matrix
W = np.outer(pattern, pattern)
np.fill_diagonal(W, 0)

print("Weight Matrix:\n", W)

# Noisy input
test = np.array([1, -1, -1, -1])

# Update rule
def update(state):
    return np.sign(W @ state)

# Run until stable
state = test
for _ in range(5):
    state = update(state)

print("Recovered Pattern:", state)
