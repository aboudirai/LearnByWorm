import pygame, sys, random
from pygame.locals import *


class WormCoords():
    
    def __init__(self,CELLSIZE):
        self.CELLSIZE = CELLSIZE
        self.wormList = []
        self.x=0
        self.y=1 
    
    def getRandomHead(self):
        xCoord = random.randint(4,12)
        yCoord = random.randint(0,15)
        #REmember to create eyes using rects
        self.wormList.append([(xCoord * self.CELLSIZE)+50,(yCoord * self.CELLSIZE)+75])
        self.wormList.append( [ self.wormList[0][self.x]-self.CELLSIZE,self.wormList[0][self.y]] )
        self.wormList.append( [ self.wormList[0][self.x]-(2*self.CELLSIZE),self.wormList[0][self.y] ] )