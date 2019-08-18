#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:04:30

@author: lungyu
'''

class JavaDrawing:
    def drawImage(self, image):
        print("Java 2D 畫 " + image)
    def drawLine(self):
        print("Java 2D 畫線 ")
    def turnImage(self, image):
        print("Java 2D 轉 " + image)
    def rotateImage(self, image):
        print("Java 2D 翻 " + image)
    
class Duke:
    def __init__(self, drawing):
        self.image = "Duke"
        self.drawing = drawing
    def move(self):
        print("計算出目的地位置")
        self.drawing.drawImage(self.image)
        self.drawing.drawLine()
    def turn(self):
        self.drawing.rotateImage(self.image)
        self.drawing.drawImage(self.image)

turtle = Duke(JavaDrawing())
turtle.move()
turtle.turn()