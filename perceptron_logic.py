import numpy as np 
class Preceptron:
  def __init__(self,learning_rate=0.1,epochs=10):
    self.lr=learning_rate
    self.epochs=epochs
    self.weights=None
    self.bias=0
  def activation_fn(self,z):
    return 1 if z>=0 else 0
  def train(self,X,y):
    n_samples,n_features = X.shape
    self.weights=np.zeros(n_features)
    self.bias =0
    for epoch in range(self.epochs):
      print(f"-----Epoch {epoch+1}-------")
      for idx,x_i in enumerate(X):
        linear_output=np.dot(x_i,self.weights)+self.bias
        y_predicted=self.activation_fn(linear_output)
        update = self.lr*(y[idx]-y_predicted)
        self.weights +=update * x_i
        self.bias +=update

  def predict(self,X):
    X = np.array(X)
    predictions =[]
    for x_i in X:
      linear_output = np.dot(x_i, self.weights)+self.bias
      y_predicted =self.activation_fn(linear_output)
      predictions.append(y_predicted)
    return np.array(predictions)
#-----AND Gate Training and Testing-----    
X = np.array([
  [0,0],
  [0,1],
  [1,0],
  [1,1]
])

y_and =np.array([0,0,0,1])
print("--Training AND Gate--")
and_preceptron =Preceptron(learning_rate=0.1,epochs=10)
and_preceptron.train(X,y_and)

print("Results for And Gate:")
for i in range(len(X)):
  prediction= and_preceptron.predict([X[i]])
  print(f"Input: {X[i]} -> Prediction: {prediction[0]}")




#-----OR Gate Training and Testing-----
  
y_or = np.array([0,1,1,1])

print("--Training OR Gate--")

or_preceptron =Preceptron(learning_rate=0.1,epochs=10)
or_preceptron.train(X,y_or)


print("Results for OR Gate:")
for i in range(len(X)):
  prediction=or_preceptron.predict([X[i]])
  print(f"Input: {X[i]} -> Prediction: {prediction[0]}")