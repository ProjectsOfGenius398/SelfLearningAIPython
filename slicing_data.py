import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[3:8])

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

dataset=loadtxt('diabetes_dataset.csv', delimiter=',')

x=dataset[:, 0:8]
y=dataset[:, 8]

print(‘value of X are:’, x)

print(‘value of Y are:’, y)