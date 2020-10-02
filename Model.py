#here we will write our training and testing data
from keras.datasets import cifar10 
from keras.utils import to_categorical
df = cifar10.load_data()
print(df.shape)
#(X_train,Y_train),(X_test,Y_test)=cifar10.load_data()
X_train=X_train/255
X_test=X_test/255
Y_train =to_categorical(Y_train,num_classes=10)
