#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:03:13

@author: lungyu
'''

class Adaptee:
    def doAction(self):
        return 'Adaptee'
 
class Adapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee
 
    def request(self):
        return self.adaptee.doAction()
 
def printIt(x):
    print(x.request())


if __name__ == '__main__':
    client = Adapter(Adaptee())
    printIt(client)