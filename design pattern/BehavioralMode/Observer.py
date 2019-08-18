#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:34:39

@author: lungyu
'''

class Client:
    def __init__(self, ip, name):
        self.ip = ip
        self.name = name
        
    # ... 其它方法...

class ClientEvent:
    pass

class ClientQueue:
    def __init__(self):
        self.clients = []
        self.listeners = []
            
    def addClientListener(self, listener):
        self.listeners.append(listener)
    
    def removeClientListener(self, listener):
        self.listeners.remove(listener)
   
    def notifyAdded(self, client):
        event = ClientEvent()
        event.ip = client.ip
        event.name = client.name
        for listener in self.listeners:
            listener.clientAdded(event)
    
    def notifyRemoved(self, client):
        event = ClientEvent()
        event.ip = client.ip
        event.name = client.name
        for listener in self.listeners:
            listener.clientRemoved(event)
          
    def add(self, client):
        self.clients.append(client)
        self.notifyAdded(client)
    
    def remove(self, client):
        self.clients.remove(client)
        self.notifyRemoved(client)    
        
    # 還有一些客戶管理佇列的其它職責....

class ClientLogger:
    def clientAdded(self, event):
        print(event.ip + " added...")
        
    def clientRemoved(self, event):
        print(event.ip + " removed...")


if __name__ == '__main__':
    queue = ClientQueue()
    queue.addClientListener(ClientLogger())
    c1 = Client("127.0.0.1", "caterpillar")
    c2 = Client("192.168.0.2", "justin")
    queue.add(c1)
    queue.add(c2)
    queue.remove(c1)
    queue.remove(c2)