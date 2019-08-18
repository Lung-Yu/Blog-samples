#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:43:48

@author: lungyu
'''

import sys
import re

# <program> ::= PROGRAM <command list> 
class Program:
    def parse(self, context):
        context.skipToken("PROGRAM")
        self.commandList = CommandList() 
        self.commandList.parse(context)

    def execute(self):
        self.commandList.execute()

# <command list> ::= <command>* END 
class CommandList:
    def parse(self, context):
        self.commands = []
        while True:
            if not context.currentToken():
                print("Missing 'END'")
                break
            elif context.currentToken() == "END":
                context.skipToken("END")
                break
            else:
                command = Command()
                command.parse(context) 
                self.commands.append(command) 

    def execute(self):
        for command in self.commands:
            command.execute()

# <command> ::= <repeat> | <primitive> 
class Command:
    def parse(self, context):
        if context.currentToken() == "REPEAT":
            self.node = Repeat()
            self.node.parse(context)
        else:
            self.node = Primitive()
            self.node.parse(context)

    def execute(self):
        self.node.execute()

# <primitive> ::= PRINT <string> | SPACE | BREAK | LINEBREAK
class Primitive:
    def parse(self, context):
        self.name = context.currentToken()
        context.skipToken(self.name)
        if (self.name != "PRINT" and
            self.name != "BREAK" and
            self.name != "LINEBREAK" and
            self.name != "SPACE"):
            print("Undefined Command")
        
        if self.name == "PRINT":
            self.text = context.currentToken()
            context.nextToken()
    
    def execute(self):
        if self.name == "PRINT":
            print self.text,
        elif self.name == "SPACE":
            print ' ',
        elif self.name == "BREAK":
            print()
        elif self.name == "LINEBREAK":
            print '\n------------------------------'

class Repeat:
    def parse(self, context):
        context.skipToken("REPEAT")
        self.number = context.currentNumber()
        context.nextToken()
        self.commandList = CommandList()
        self.commandList.parse(context)
    
    def execute(self):
        for i in range(self.number):
            self.commandList.execute()

class Context:
    def __init__(self, filename):
        tokenList = []
        for line in open(filename):
            for token in re.split("\s+", line.strip()):
                tokenList.append(token)
        self.tokens = iter(tokenList)
        self.nextToken()
    
    def nextToken(self):
        self.current = None
        try:
            self.current = next(self.tokens)
        except StopIteration: 
            pass
        return self.current
       
    def currentToken(self):
        return self.current
    
    def skipToken(self, token):
        if token != self.current:
            print("Warning: " + token + 
                  " is expected, but " + 
                  self.currentToken + " is found.");
        self.nextToken()

    def currentNumber(self):
        return int(self.current)
if __name__ == '__main__':
    node = Program()
    node.parse(Context(sys.argv[1]))
    node.execute()

