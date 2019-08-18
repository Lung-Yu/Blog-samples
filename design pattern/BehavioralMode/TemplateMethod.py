#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:28:58

@author: lungyu
'''


import random
from abc import ABCMeta, abstractmethod

class GuessGame():
    
    @abstractmethod
    def message(self, msg):
        pass

    @abstractmethod
    def guess(self):
        pass     

    def go(self):
        self.message(self.welcome)
        number = int(random.random() * 10)
        while True:
            guess = self.guess();
            if guess > number:
                self.message(self.bigger)
            elif guess < number:
                self.message(self.smaller)
            else:
                break
        self.message(self.correct)

class ConsoleGame(GuessGame):
    def __init__(self):
        self.welcome = "歡迎"
        self.prompt = "輸入數字："
        self.correct = "猜中了"
        self.bigger = "你猜的比較大"
        self.smaller = "你猜的比較小"
    
    def message(self, msg):
        print(msg)
    
    def guess(self):
        return int(input(self.prompt))

game = ConsoleGame()
game.go()