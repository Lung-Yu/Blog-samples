#-*- encoding: utf-8 -*-
'''
Created on 2016-09-26 00:26:35

@author: lungyu
'''

import SocketServer

class EchoHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline().strip()
        self.wfile.write(self.data)

server = SocketServer.TCPServer(("localhost", 9999), EchoHandler)
server.serve_forever()