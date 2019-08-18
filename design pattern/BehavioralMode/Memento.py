#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:39:14

@author: lungyu
'''

import time
class Backup:
    def __init__(self, state):
        self.state = state
        self.date = time.ctime()

class Application:
    def __init__(self):
        self.state = "default setting"
        
    def backup(self):
        return Backup(self.state)
    
    def recover(self, backup):
        self.state = backup.state

class Recovery:
    def __init__(self):
        self.backups = []
    
    def add(self, backup):
        self.backups.append(backup)
    
    def retrieve(self, date):
        for backup in self.backups:
            if backup.date == date:
                self.backups.remove(backup)
                return backup
        return None
    
if __name__ == '__main__':
    application = Application()
    recovery = Recovery()
            
    print(application.state)
            
    backup = application.backup()  # 建立備忘
    recovery.add(backup) # 加入備忘錄
            
    application.state = "customer setting"
    print(application.state)
            
    date = backup.date; # 假設 date 是使用者自行設定所要取得的還原時間！
    application.recover(recovery.retrieve(date)) # 取得備忘來還原
    print(application.state)
