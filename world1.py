import pygame
import random as r
from agent import Agent

class World:
    def __init__(self, scrWidth, scrHeight, caption):
        pygame.init()
        self.colors = {'RED'   : (255,   0,   0),
                       'GREEN' : (  0, 150,   0),
                       'BLUE'  : (  0,   0, 255),
                       'BROWN' : (165,  42,  42),
                       'BLACK' : (  0,   0,   0),
                       'WHITE' : (255, 255, 255)}
        self.SIZE = (scrWidth, scrHeight)
        self.display = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption(caption)

        self.nPixels = 40
        self.pixelSize = 20
        self.board = []

        self.bridges = []

        self.agents = []

        self.initialState()

    def initialState(self):
        for row in range(self.nPixels):
            self.board.append([])
            for column in range(self.nPixels):
                self.board[row].append('*' if (r.random() < 0.3) else '-')

        '''
        for i in range(4):
            row = r.randint(rowsList[i][0], rowsList[i][1]-1)
            col = r.randint(columnsList[0][0], columnsList[0][1]-1) if i % 2 == 0
                else r.randint(columnsList[1][0], columnsList[1][1]-1)
            a = Agent(self.colors['RED'], row, col)
            self.addAgent(a)
        '''

    def addAgent(self, agent):
        self.agents.append(agent)

    def addBridge(self, bridge):
        self.bridges.append(bridge)

    def update(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return False

        self.randomWorld()

        return True

    def draw(self):
        for row in range(self.nPixels):
            for column in range(self.nPixels):
                if (self.board[row][column] == '*'):
                    color = self.colors['BLUE']
                elif (self.board[row][column] == '-'):
                    color = self.colors['GREEN']

                pygame.draw.rect(self.display, color,
                                [self.pixelSize*column, self.pixelSize*row,
                                self.pixelSize, self.pixelSize])



        for agent in self.agents:
            pygame.draw.rect(self.display, agent.color,
                        [self.pixelSize*agent.pos[1],
                         self.pixelSize*agent.pos[0],
                         self.pixelSize,self.pixelSize])

        pygame.display.flip()

    def randomWorld(self):
        for i in range(2):
            row = r.randint(0,len(self.board)-1)
            col = r.randint(0,len(self.board)-1)
            if (self.board[row][col] == '-'):
                self.board[row][col] = '*'
            elif (self.board[row][col] == '*'):
                self.board[row][col] = '-'

    def displayGrid(self):
        for row in self.board:
            print(row)
