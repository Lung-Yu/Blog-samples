#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:24:42

@author: lungyu
'''
class NumberGenerator:
    
    class Iterator:
        def __init__(self, length):
            self.length = length
            self.number = -1
        def __next__(self):
            self.number = self.number + 1
            if self.number == self.length:
                raise StopIteration
            return self.number
    
    def __init__(self, length):
        self.length = length

    def __iter__(self):
        return NumberGenerator.Iterator(self.length)

for n in NumberGenerator(10):
    print(n)