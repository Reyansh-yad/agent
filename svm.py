import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Create Dataset
X = np.array([[1,2], [2,3], [3,3], [6,5], [7,7], [8,6]])
y = np.array([0,0,0,1,1,1])

# Step 2: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create SVM Model
model = svm.SVC(kernel='linear')   # Linear Kernel

# Step 4: Train Model
model.fit(X_train, y_train)

# Step 5: Predict
y_pred = model.predict(X_test)

# Step 6: Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Predicted:", y_pred)
print("Accuracy:", accuracy)
