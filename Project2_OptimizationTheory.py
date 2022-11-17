import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Import the data (taken from MATLAB File):
#Y data provides the pixel information of the image
#C data provides the classification of the data
Ctest = pd.read_csv('Ctest.csv')
Ytest = pd.read_csv('Ytest.csv')
Ctrain = pd.read_csv('Ctrain.csv')
Ytrain = pd.read_csv('Ytrain.csv')

#Data reshaped to 28x28 to match image size
Ytrain_reshape = np.reshape(np.array(Ytrain), (len(Ytrain), 28, 28))
Ytest_reshape = np.reshape(np.array(Ytest), (len(Ytest), 28, 28))

#Plotting Images
#Generate 12 pseudo random number for selecting visualization
random_digits = np.random.randint(0,len(Ytrain_reshape), 12)

for i in range(len(random_digits)):
    plt.figure(i)
    plt.imshow(Ytrain_reshape[random_digits[i]], cmap = 'gray')