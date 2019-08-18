#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:16:08

@author: lungyu
'''

import weakref

class Style:
    PLAIN = 1
    BOLD = 2
    ITALIC = 3

class Font:
    def __init__(self, name, style, size):
        self.name = name
        self.style = style
        self.size = size
    def __repr__(self):
        return repr(self.name) + repr(self.style) + repr(self.size)

class FontFactory:
    __flyweight = weakref.WeakValueDictionary()
    
    @staticmethod
    def create(name, style, size):
        font = Font(name, style, size)
        if not FontFactory.__flyweight.get(repr(font), None):
            FontFactory.__flyweight[repr(font)] = font
        return FontFactory.__flyweight[repr(font)]
    
if __name__ == '__main__':
    font1 = FontFactory.create("細明體", Style.BOLD, 12)
    font2 = FontFactory.create("細明體", Style.BOLD, 12)
    print font1 is font2