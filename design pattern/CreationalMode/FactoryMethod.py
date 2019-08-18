#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:00:15

@author: lungyu
'''

class Editor:
    def __init__(self):
        self.docs = []
    def open(self, file):
        doc = self.createDocument()
        doc.title = file
        doc.open()
        self.docs.append(doc)
    def save(self, doc):
        doc.save()
    def close(self, doc=None):
        if doc:
            doc.close()
            self.docs.remove(doc)
        else:
            for doc in self.docs:
                self.close(doc)

class TextDoc:
    def open(self):
        print("開啟文字檔案 " + self.title)
    def save(self):
        print("儲存文字檔案 " + self.title)
    def close(self):
        print("關閉文字檔案 " + self.title)
 
class TextEditor(Editor):
    def createDocument(self):
        doc = TextDoc()
        # ...
        return doc

editor = TextEditor()
editor.open("app.py")
editor.open("editor.py")
editor.close()