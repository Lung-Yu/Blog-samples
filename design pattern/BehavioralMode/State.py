#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:36:50

@author: lungyu
'''
import time

class Red:
    def change(self, light):
        print("紅燈")
        time.sleep(5)
        light.set(Green())

class Green:
    def change(self, light):
        print("綠燈")
        time.sleep(5)
        light.set(Yellow())

class Yellow:
    def change(self, light):
        print("黃燈")
        time.sleep(1)
        light.set(Red())

class TrafficLight:
    def __init__(self):
        self.current = Red()
    
    def set(self, state):
        self.current = state
    
    def change(self):
        self.current.change(self)

if __name__ == '__main__':
    trafficLight = TrafficLight()
    while True:
        trafficLight.change()