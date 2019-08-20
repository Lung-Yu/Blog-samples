import numpy as np

class Encoder(object):
    def __init__(self,class_number,start_with=0):
        self._start_with = 0
        self._n_class = class_number
    
    def one_hot_encode(self,x):
        y = np.zeros(self._n_class,dtype=float)
        y[x - self._start_with] = 1
        return y
    
    def label(self,X):
        return np.argmax(X) + self._start_with