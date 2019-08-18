#-*- encoding: utf-8 -*-
'''
Created on 2016-09-25 23:42:45

@author: lungyu
'''

class Singleton:
    __single = None
    def __init__(self):
        if Singleton.__single:
            raise Singleton.__single
        Singleton.__single = self
    
    @staticmethod
    def getSingleton():
        if not Singleton.__single:
            Singleton.__single = Singleton()
        return Singleton.__single
    
    def doSomething(self):
        print("do something...XD")
        
if __name__ == '__main__':
    singleton = Singleton.getSingleton()
    singleton.doSomething()