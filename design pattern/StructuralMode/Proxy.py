#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:18:22

@author: lungyu
'''

class Image:
    ...
    def draw(self):
        ...

class ImageProxy:
    def __init__(self, filename):
        self.image = None
        self.filename = filename
    def draw(self):
        if not self.image:
            self.image = Image(filename)
        self.image.draw()

class Document:
    def __init__(self):
        self.image = ImageProxy("doc://images/xxx.jpg")
    def scroll(self):
        ...
        self.image.draw()