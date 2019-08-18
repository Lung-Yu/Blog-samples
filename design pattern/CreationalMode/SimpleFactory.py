#-*- encoding: utf-8 -*-
'''
Created on 2016-09-25 23:50:11

@author: lungyu
'''

class Message:
    def __init__(self, addr, msg):
        self.addr = addr
        self.msg = msg
    
    @classmethod
    def send(self):
        print("send message '%s' to '%s'" % (self.msg, self.addr))
        

class MessageFactory:
    
    @staticmethod
    def getMessage(addr,msg):
        message = Message('a','b')
        return message

if __name__ == '__main__':
    msg = MessageFactory.getMessage('caterpillar@openhome.cc', 'Hi')
    msg.send()