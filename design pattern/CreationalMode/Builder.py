# -*- encoding: utf-8 -*-
'''
Created on 2016-09-25 23:42:23

@author: lungyu
'''

class Exhibition:
    def __init__(self, maze):
        self.maze = maze
    def paint(self):
        for row in self.maze :
            for c in row :
                print c ,
            print ''

class ExhibitionBuilder:
    def __init__(self, rowSize, columnSize):
        self.maze = [[''] * columnSize for i in range(rowSize)]
    def builDaisle(self, i, j):
        self.maze[i][j] = ' '
    def buildWall(self, i, j):
        self.maze[i][j] = '*'
    def buildHorizontalBooth(self, i, j):
        self.maze[i][j] = '_'
    def buildVerticalBooth(self, i, j):
        self.maze[i][j] = '|'
    def getExhibition(self):
        return Exhibition(self.maze)

class ExhibitionDirector:
    def __init__(self, maze, builder):
        self.maze = maze
        self.builder = builder
    def build(self):
        for i in range(len(self.maze)) :
            for j in range(len(self.maze[i])) :
                if(self.maze[i][j] == 0):
                    self.builder.builDaisle(i, j);
                elif(self.maze[i][j] == 1):
                    self.builder.buildWall(i, j);
                elif(self.maze[i][j] == 2):
                    self.builder.buildVerticalBooth(i, j);
                elif(self.maze[i][j] == 3):
                    self.builder.buildHorizontalBooth(i, j);
        return self.builder.getExhibition()

material = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 3, 0, 0, 2, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 1],
            [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]


if __name__ == '__main__':
    builder = ExhibitionBuilder(len(material), len(material[0]))  # make map
    director = ExhibitionDirector(material, builder)
    director.build().paint()
