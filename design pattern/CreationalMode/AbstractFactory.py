#-*- encoding: utf-8 -*-
'''
Created on 2016-09-25 23:57:54

@author: lungyu
'''

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def paint(self, factory):
        point = factory.getPoint()
        corner = factory.getCorner()
        corner.leftUp()
        point.line(self.width - 2)
        corner.rightUp()
        print()
        for i in range(self.height - 2):
            point.line(self.width)
            print()        
        corner.leftDown()
        point.line(self.width - 2);
        corner.rightDown();
        print()
        
class Dot:
    def line(self, width):
        for i in range(width):
            print "-",

class Sharp:
    def leftUp(self):
        print "#",
    def rightUp(self):
        print "#",
    def leftDown(self):
        print "#",
    def rightDown(self):
        print "#",

class DotSharpFactory:
    def getPoint(self):
        return Dot()
    def getCorner(self):    
        return Sharp()
        
rect = Rectangle(20, 10)
rect.paint(DotSharpFactory())