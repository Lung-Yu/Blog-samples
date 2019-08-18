#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:07:52

@author: lungyu
'''

class FriedChicken:
    def getContent(self):
        return "不黑心炸雞"
    def price(self):
        return 49.0

class Hamburger:
    def getContent(self):
        return "美味蟹堡"
    def price(self):
        return 99.0
        
class SideDish:
    def __init__(self, meal):
        self.meal = meal

class SideDishOne(SideDish):
    def __init__(self, meal):
        SideDish.__init__(self, meal)
        
    def getContent(self):
        return self.meal.getContent() + " | 可樂 | 薯條"
    
    def price(self):
        return self.meal.price() + 30.0

meal = SideDishOne(FriedChicken())
print("點了：" + meal.getContent())
print("價格：" + str(meal.price()))