import gzip
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

train_data = "train-images-idx3-ubyte.gz"
train_labels = "train-labels-idx1-ubyte.gz"

test_data = "t10k-images-idx3-ubyte.gz"
test_labels = "t10k-labels-idx1-ubyte.gz"

def mnist_images(filename):
    with gzip.open(filename, 'rb') as file:
        data = np.frombuffer(file.read(), np.uint8, offset = 16)
        return data.reshape(-1, 28, 28) / 255

def mnist_labels(filename):
    with gzip.open(filename, 'rb') as file:
        data = np.frombuffer(file.read(), np.uint8, offset = 8)
        return data

X_train = mnist_images(train_data)
y_train = mnist_labels(train_labels)

X_test = mnist_images(test_data)
y_test = mnist_labels(test_labels)
#print(X_train[0].reshape(784))

print(y_train[50])
plt.imshow(X_train[50])
plt.show()

scaler = StandardScaler()
scaler.fit(X_train.reshape(-1, 784))
 
X_train = scaler.transform(X_train.reshape(-1, 784))
X_test = scaler.transform(X_test.reshape(-1, 784))

model = SVC(kernel = "rbf", gamma = 0.001, C = 10)
model.fit(X_train.reshape(-1, 784), y_train)

print(model.score(X_test.reshape(-1, 784), y_test))
