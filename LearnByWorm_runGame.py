import random,pygame, sys
from pygame.locals import *
from WormCoords import WormCoords

#LearnByWorm

pygame.init()

FPS = 10
FPSCLOCK = pygame.time.Clock()
    
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

WINDOWWIDTH = 500
WINDOWHEIGHT = 500

x = 0
y = 1

basicFont = pygame.font.SysFont(None,48)
numFont = pygame.font.SysFont(None,32)


headIndex = 0
isMoving = True

windowSurface = pygame.display.set_mode( (WINDOWWIDTH,WINDOWHEIGHT), 0 ,32 )
pygame.display.set_caption("LearnByWorm")

CELLSIZE = 25;
CELLROW = (WINDOWWIDTH-100) / CELLSIZE
CELLCOL = (WINDOWHEIGHT-100) / CELLSIZE

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

wormDir = RIGHT
#firstStart = False

windowSurface.fill(BLUE)

WORMHEAD = 0
WORMCOLOR = RED;
wormCoords = WormCoords(CELLSIZE)

sumNum = 14

footer = numFont.render("Kids Learn. They LearnByWorm",True,BLACK)
footerRect = footer.get_rect()
footerRect.topleft = (15,WINDOWHEIGHT-20)


'''
titleText = basicFont.render("LearnByWorm",True,BLACK);
titleRect = titleText.get_rect()
titleRect.topleft = (0,0)
'''
problemText = basicFont.render("__ + __ = 14",True,BLACK)
problemRect = problemText.get_rect()

#titleRect.topleft=(WINDOWWIDTH,0)
problemRect.topleft = (WINDOWWIDTH/2-100,10)
windowSurface.blit(footer,footerRect)

FLOORTOPLEFTX = 50
FLOORTOPLEFTY = 75
FLOORBOTRIGHTX = WINDOWWIDTH - 100
FLOORBOTRIGHTY = WINDOWHEIGHT - 100

#windowSurface.blit(titleText,titleRect)
windowSurface.blit(problemText,problemRect)

def main():
    while True:
        #waitForKey();
        runGame()
        


def waitForKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    pygame.QUIT()
                    sys.exit()
                return
def randomNumSpawn():
    numOfNums = 5;
    count = 0
    nums = []
    while count < 5:
        randAdd = random.randint(1,9)
        randX = random.randint(0,15)
        randY = random.randint(0,15)
        #cellPosX = (randX * CELLSIZE) + 55
        #cellPosY = (randY * CELLSIZE) + 78
        #newText = numFont.render(str(randAdd),True,BLACK)
        #newTextRect = newText.get_rect()
        #newTextRect.topleft = (55 + (CELLSIZE * randX), 78 + (CELLSIZE * randY))
        nums.append([randAdd,randX,randY,])
        count += 1
    return nums

numsList = randomNumSpawn()


def drawFloor():
    #Vertical Lines
    randomNumSpawn()
    wormFloor = (FLOORTOPLEFTX,FLOORTOPLEFTY,CELLCOL*CELLSIZE,CELLROW*CELLSIZE)
    pygame.draw.rect(windowSurface,RED,wormFloor)

    for i in range(50,WINDOWWIDTH-50,CELLSIZE):
        pygame.draw.line(windowSurface, BLACK, (i,FLOORTOPLEFTY), (i,FLOORBOTRIGHTY+75))
    #Horizontal Lines
    for i in range(75,WINDOWHEIGHT,CELLSIZE):
        pygame.draw.line(windowSurface,BLACK, (50,i),(FLOORBOTRIGHTX + 50,i))
    
    
    for i in numsList:
        randAdd = i[0]
        numPosX = i[1]
        numPosY = i[2]
        
        newText = numFont.render(str(randAdd),True,BLACK)
        newTextRect = newText.get_rect()
        topLeftX = 55 + (CELLSIZE * numPosX)
        topLeftY = 78 + (CELLSIZE * numPosY)
        newTextRect.topleft = (topLeftX,topLeftY)
        windowSurface.blit(newText,newTextRect)
    
    #FIX THE AUTO ALGORITHM
    
    #addList = [randAdd1,randAdd2,randX1,randY1,randX2,randY2]
    
    newText1 = numFont.render(str(perfectMatchList[0]),True,BLACK)
    newText2 = numFont.render(str(perfectMatchList[1]),True,BLACK) 
    newText1Rect = newText1.get_rect()
    newText2Rect = newText2.get_rect()
    topLeftX1 = 55 + (CELLSIZE * perfectMatchList[2])
    topLeftY1 = 78 + (CELLSIZE * perfectMatchList[3])
    topLeftX2 = 55 + (CELLSIZE * perfectMatchList[4])
    topLeftY2 = 78 + (CELLSIZE * perfectMatchList[5])
    newText1Rect.topleft = (topLeftX1,topLeftY1 )
    newText2Rect.topleft = (topLeftX2,topLeftY2 )
    windowSurface.blit(newText1,newText1Rect)
    windowSurface.blit(newText2,newText2Rect)
        
        #newTextRect.topleft = (55 + (CELLSIZE * numPosX ), 78 + (CELLSIZE * numPosY))
        #nums.append([randAdd,randX,randY,])
        
        
    
def drawWorm():
    for i in wormCoords.wormList:
        iRect = (i[x],i[y],CELLSIZE,CELLSIZE)
        pygame.draw.rect(windowSurface,GREEN,iRect)
    for i in wormCoords.wormList:
        iRect = (i[x] + CELLSIZE / 2,i[y] + CELLSIZE / 2,CELLSIZE / 4,CELLSIZE / 4)
        pygame.draw.rect(windowSurface,BLACK,iRect)
        
def moveWorm():
    delPos = len(wormCoords.wormList)-1
    del wormCoords.wormList[delPos]
    if wormDir == RIGHT:
        newHead = [wormCoords.wormList[0][x] + CELLSIZE,wormCoords.wormList[0][y]]
    elif wormDir == LEFT:
        newHead = [wormCoords.wormList[0][x] - CELLSIZE,wormCoords.wormList[0][y]]
    elif wormDir == UP:
        newHead = [wormCoords.wormList[0][x],wormCoords.wormList[0][y] - CELLSIZE]
    elif wormDir == DOWN:
        newHead = [wormCoords.wormList[0][x],wormCoords.wormList[0][y] + CELLSIZE]
    wormCoords.wormList.insert(0, newHead)
    
wormCoords.getRandomHead()    

   
def checkForDeath():
    print("In the Loop")
    if wormCoords.wormList[headIndex][x] > ((CELLROW*CELLSIZE)):
        return True
    elif wormCoords.wormList[headIndex][y] > (25 + (CELLCOL*CELLSIZE)):
        return True
    elif wormCoords.wormList[headIndex][x] < (75):
        return True
    elif wormCoords.wormList[headIndex][y] < (100):
        return True
    else:
        return False

def getAutoMatch():
    randAdd1 = random.randint(5,9)
    randAdd2 = sumNum - randAdd1
    randX1 = random.randint(0,15)
    randY1 = random.randint(0,15)
    randX2 = random.randint(0,15)
    randY2 = random.randint(0,15)
    addList = [randAdd1,randAdd2,randX1,randY1,randX2,randY2]
    return addList

perfectMatchList = getAutoMatch()

def runGame():
    wormDir = RIGHT
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    print("LEfty")
                    if wormDir != RIGHT and wormDir != LEFT:
                        wormDir = LEFT
                elif event.key == K_RIGHT:
                    if wormDir != RIGHT and wormDir != LEFT:
                        wormDir = RIGHT
                elif event.key == K_UP:
                    if wormDir != DOWN and wormDir != UP:
                        wormDir = UP
                elif event.key == K_DOWN:
                    if wormDir != DOWN and wormDir != UP:
                        wormDir = DOWN
                    
        if checkForDeath() == True:
            return
        moveWorm()
        drawFloor()
        drawWorm()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

main()
