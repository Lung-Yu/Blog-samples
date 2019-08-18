#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:06:13

@author: lungyu
'''

class Frame:
    def __init__(self, image):
        self.image = image
    def play(self):
        print("播放 " + self.image)

class Playlist:
    def __init__(self):
        self.list = []
    def add(self, playable):
        self.list.append(playable);
    def play(self):
        for playable in self.list:
            playable.play()


if __name__ == '__main__':
    logo = Frame("片頭 LOGO")
        
    playlist1 = Playlist()
    playlist1.add(Frame("Duke 左揮手"))
    playlist1.add(Frame("Duke 右揮手"))
        
    playlist2 = Playlist()
    playlist2.add(Frame("Duke 走左腳"))
    playlist2.add(Frame("Duke 走右腳"))
    
    all = Playlist()
    all.add(logo)
    all.add(playlist1)
    all.add(playlist2)
    
    all.play();