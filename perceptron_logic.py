import numpy as np 
class Preceptron:
  def _init_(self,learning_rate=0.1,epoches=10):
    self.lr=learning_rate
    self.epoches=epoches
    self.weight=None
    self.bais=None
  def activation_fn(slef,z):
    return 1 if z>=0 else 0
  def train(slef,X,y):
    n_smaples,n_features = X.shape
    self.weights=np.zeros(n_features)
    self.bias =0
    for epoches in range(self.epoches):
      print(f"-----{epoches+1}-------")
      for idx,x_i in enumerate(X):
        linear_output=np.dot(x_i,self.weights)+slef.bais
        y_predicted=self.activation_fn(linear_output)
        update = self.lr*(y[idx]-predicted)
        slef.weights +=update * x_i
        slef.bais +=update
    
    def predict(self,X):
      predictions =[]
      for x_i in X:
        linear_ouput = np.dot(x_i, self.weights)+slef.bias
        y_predicted =self.activation_fn(linear_output)
        predictions.append(y_predicted)
      return np.array(predictions)




  
