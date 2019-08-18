#-*- encoding: utf-8 -*-
'''
Created on 2016-09-25 23:42:34

@author: lungyu
'''
import copy

class Wheel:
    def clone(self):
        return copy.deepcopy(self)

class Car:
    def __init__(self):
        self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
    def clone(self):
        return copy.deepcopy(self)

class Cars:
    def __init__(self):
        self.prototypes = {}
    def addPrototype(self, brand, car):
        self.prototypes[brand] = car
    def getPrototype(self, brand):
        return self.prototypes[brand].clone()


if __name__ == '__main__':
    bmw = Car()
    benz = Car()
    cars = Cars()
    cars.addPrototype("BMW", bmw)
    cars.addPrototype("BENZ", benz)
    bmwPrototype = cars.getPrototype("BMW")