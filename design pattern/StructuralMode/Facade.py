#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:09:21

@author: lungyu
'''

class Some:        
    def doSomething(self):
        print 'Some'

class Other:
    def doSomething(self):
        print 'Other'

class Another :
    def doSomething(self):
        print 'AnOther'

class ActionService:
    def doAction(self):
        some = Some()
        other = Other()
        another = Another()
        # 作一些互動以產生結果
        some.doSomething()
        other.doSomething()
        another.doSomething()

class Application:    
    def __init__(self, service):
        self.service = service
    
    def doAction(self):
        self.service.doAction()

if __name__ == '__main__':
    Application(ActionService()).doAction()