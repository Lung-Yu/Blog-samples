#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:41:55

@author: lungyu
'''

class Customer:
    def doCustomer(self):
        print("客戶服務")
    
    def pay(self):
        print("結帳")
    
    def accept(self, visitor): pass

class Member(Customer):
    def doMember(self):
        print("會員服務")
    
    def accept(self, visitor):
        visitor.visitMember(self)
    
class VIP(Customer):
    def doVIP(self):
        print("VIP 服務")
        
    def accept(self, visitor):
        visitor.visitVIP(self)

class VisitorImpl:
    def visitMember(self, member):
        member.doMember();
    
    def visitVIP(self, vip):
        vip.doVIP()
    
class Service:
    def __init__(self):
        self.visitor = VisitorImpl()
    
    def doService(self, customer):
        customer.doCustomer()
        customer.accept(self.visitor)
        customer.pay()

if __name__ == '__main__':
    service = Service()
    service.doService(VIP())