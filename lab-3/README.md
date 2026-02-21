# Lab 3 — Machine Learning Algorithms

Implementations of fundamental supervised and unsupervised machine learning algorithms built from scratch with NumPy, plus a scikit-learn SVM example.

## Overview

This lab covers core machine learning techniques:

- **Perceptron** — single-layer linear classifier for logic gates
- **Neural Network (XOR)** — two-layer backpropagation network
- **K-Nearest Neighbours (KNN)** — instance-based lazy learner
- **K-Means Clustering** — unsupervised centroid-based clustering
- **Support Vector Machine (SVM)** — maximum-margin linear classifier via scikit-learn
- **Hopfield Network** — recurrent associative memory for noisy pattern recovery
- **Bidirectional Associative Memory (BAM)** — two-way pattern association
- **Odd/Even Classifier** — perceptron detecting number parity

## Files

| File | Description |
|------|-------------|
| `perceptron_logic.py` | Perceptron trained on AND and OR logic gates |
| `X_OR.py` | Two-layer neural network solving the XOR problem via backpropagation |
| `KNN.py` | K-Nearest Neighbours classifier built from scratch |
| `kmean.py` | K-Means clustering algorithm built from scratch |
| `svm.py` | Linear SVM classifier using scikit-learn |
| `Hopfield.py` | Hopfield network for bipolar pattern storage and noisy-input recovery |
| `Bi-dir.py` | Bidirectional Associative Memory (BAM) for associating pattern pairs |
| `odd&even.py` | Perceptron-based classifier for odd/even number detection |

## Program Details

### `perceptron_logic.py` — Perceptron for Logic Gates

Implements a single-layer perceptron with a step activation function. Trains and tests the model on the AND and OR truth tables.

**Key Components:**
- `Perceptron` class with `train()` and `predict()` methods
- Configurable `learning_rate` and `epochs`
- Step activation: outputs 1 if `z ≥ 0`, else 0
- Weight update rule: `w += lr * (y - ŷ) * x`

**Example output:**
```
Results for And Gate:
Input: [0 0] -> Prediction: 0
Input: [0 1] -> Prediction: 0
Input: [1 0] -> Prediction: 0
Input: [1 1] -> Prediction: 1
```

> **Note:** A single-layer perceptron cannot solve XOR (it is not linearly separable). The XOR gate section in this file contains intentional syntax errors demonstrating this limitation; use `X_OR.py` instead.

---

### `X_OR.py` — XOR Neural Network (Backpropagation)

A two-layer (one hidden layer) feedforward neural network trained with backpropagation to solve the XOR problem.

**Architecture:**
- Input layer: 2 neurons
- Hidden layer: 4 neurons, sigmoid activation
- Output layer: 1 neuron, sigmoid activation

**Training:**
- 10 000 epochs, learning rate 0.1
- Forward pass → compute error → backpropagate gradients → update weights

**Example output:**
```
Results for XOR Gate:
Input: [0 0] -> Prediction: 0
Input: [0 1] -> Prediction: 1
Input: [1 0] -> Prediction: 1
Input: [1 1] -> Prediction: 0
```

---

### `KNN.py` — K-Nearest Neighbours

A from-scratch KNN classifier using Euclidean distance and majority voting.

**Key Components:**
- `euclidean_distance(x1, x2)` — computes L2 distance
- `KNN` class with `fit()` and `predict()` methods
- Configurable `k` (default 3)
- Majority vote among the k nearest training samples

**Example:**
```python
model = KNN(k=3)
model.fit(X_train, y_train)
print(model.predict([[5, 5]]))   # [1]
```

---

### `kmean.py` — K-Means Clustering

A from-scratch K-Means implementation using NumPy vectorised operations.

**Algorithm:**
1. Initialise centroids to the first k data points
2. Assign each point to its nearest centroid
3. Recompute centroids as cluster means
4. Repeat until centroids converge

**Key Components:**
- `KMeans` class with `fit()` and `predict()` methods
- Configurable `k` and `max_iters`
- Convergence check: stops when centroids stop moving

**Example output:**
```
Centroids:
[[2.  2.67]
 [7.  6.  ]]
Cluster Labels:
[0 0 0 1 1 1]
```

---

### `svm.py` — Support Vector Machine

Uses scikit-learn's `SVC` with a linear kernel to classify a small dataset.

**Steps:**
1. Create labelled dataset (two linearly separable classes)
2. Split into train/test sets (`test_size=0.2`)
3. Train `SVC(kernel='linear')`
4. Predict on test set and report accuracy

**Example output:**
```
Predicted: [0 0]
Accuracy: 1.0
```

---

### `Hopfield.py` — Hopfield Network

A single-layer recurrent associative memory that stores a bipolar pattern as a weight matrix and recovers it from a noisy input.

**Algorithm:**
1. Compute weight matrix: `W = pattern ⊗ pattern` (outer product), zero diagonal
2. Iterative update: `state = sign(W · state)` until convergence

**Example output:**
```
Weight Matrix:
 [[ 0 -1  1 -1]
 [-1  0 -1  1]
 [ 1 -1  0 -1]
 [-1  1 -1  0]]
Recovered Pattern: [ 1 -1  1 -1]
```

---

### `Bi-dir.py` — Bidirectional Associative Memory (BAM)

Associates two bipolar pattern vectors so that each can be recalled from the other using a shared weight matrix.

**Algorithm:**
- Weight matrix: `W = Xᵀ · Y`
- Recall Y from X: `y = sign(x · W)`
- Recall X from Y: `x = sign(y · Wᵀ)`

**Example output:**
```
Weight Matrix:
 [[ 1  1 -1]
 [-1 -1  1]
 [ 1  1 -1]]
Recall Phone from ID: [[ 1  1 -1]]
Recall ID from Phone: [[ 1 -1  1]]
```

---

### `odd&even.py` — Odd/Even Perceptron Classifier

A single-neuron perceptron that learns to classify numbers as odd or even based on the last binary digit.

**Key Components:**
- Trains on input `{0 → even, 1 → odd}` using the perceptron learning rule
- Sign activation: outputs `1` (even) or `-1` (odd)
- Accepts user input at runtime for live classification

**Example output:**
```
Trained weight: [0.1]
Trained bias: 0.1
Enter number: 4
Even Number
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- NumPy
- scikit-learn (for `svm.py` only)

### Installation

```bash
git clone https://github.com/Reyansh-yad/agent.git
cd agent
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

### Running the Programs

```bash
# Perceptron for AND / OR gates
python lab-3/perceptron_logic.py

# XOR via backpropagation neural network
python lab-3/X_OR.py

# K-Nearest Neighbours
python lab-3/KNN.py

# K-Means Clustering
python lab-3/kmean.py

# Support Vector Machine
python lab-3/svm.py

# Hopfield network pattern recovery
python lab-3/Hopfield.py

# Bidirectional Associative Memory
python lab-3/Bi-dir.py

# Odd/Even perceptron classifier
python "lab-3/odd&even.py"
```

## Key Concepts

| Concept | Algorithm | File |
|---------|-----------|------|
| Linear classification | Perceptron | `perceptron_logic.py` |
| Non-linear classification | Backpropagation NN | `X_OR.py` |
| Instance-based learning | KNN | `KNN.py` |
| Unsupervised clustering | K-Means | `kmean.py` |
| Maximum-margin classifier | SVM | `svm.py` |
| Recurrent associative memory | Hopfield Network | `Hopfield.py` |
| Bidirectional associative memory | BAM | `Bi-dir.py` |
| Binary classification (perceptron) | Odd/Even | `odd&even.py` |

## Dependencies

- `numpy` — array operations and distance calculations
- `scikit-learn` — SVM implementation and train/test split
- Python standard library only for remaining files

## License

MIT License — free to use for educational and research purposes.
