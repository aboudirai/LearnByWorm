import random, pygame, sys

from pygame.locals import *
from WormCoords import WormCoords


#LearnByWorm
pygame.init()

FPS = 7
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
startFont = pygame.font.SysFont(None,64)



headIndex = 0
newHead = 0
isMoving = True

windowSurface = pygame.display.set_mode( (WINDOWWIDTH,WINDOWHEIGHT), 0 ,32 )
pygame.display.set_caption("LearnByWorm")

#IMAGE WONT LOAD
image = pygame.image.load("pics/pencil.png")
imageRect = image.get_rect()
imageRect.topleft = (5,20)
windowSurface.blit(image,imageRect)

CELLSIZE = 25;
CELLROW = (WINDOWWIDTH-100) / CELLSIZE
CELLCOL = (WINDOWHEIGHT-100) / CELLSIZE

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

wormDir = RIGHT
#firstStart = False


WORMHEAD = 0
WORMCOLOR = RED;
wormCoords = WormCoords(CELLSIZE)

sumNum = 14

footer = numFont.render("Kids Learn. They LearnByWorm",True,BLACK)
footerRect = footer.get_rect()
footerRect.topleft = (15,WINDOWHEIGHT-20)

problemText = basicFont.render("__ + __ = 14",True,BLACK)
problemRect = problemText.get_rect()
problemRect.topleft = (WINDOWWIDTH/2-100,10)    
    
add1 = 0
add2 = 0
detCount = 0
'''
titleText = basicFont.render("LearnByWorm",True,BLACK);
titleRect = titleText.get_rect()
titleRect.topleft = (0,0)
'''

windowSurface.blit(footer,footerRect)

addList = [0,0]

FLOORTOPLEFTX = 50
FLOORTOPLEFTY = 75
FLOORBOTRIGHTX = WINDOWWIDTH - 100
FLOORBOTRIGHTY = WINDOWHEIGHT - 100
    
#windowSurface.blit(titleText,titleRect)
oneNumDet = 0

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
    while count < 4:
        randChoice = random.randint(0,3)
        if randChoice == 0:
            randAdd = random.randint(1,9)
        else:
            randAdd = random.randint(5,9)
        randX = random.randint(1,14)
        randY = random.randint(1,14)
        #cellPosX = (randX * CELLSIZE) + 55
        #cellPosY = (randY * CELLSIZE) + 78
        #newText = numFont.render(str(randAdd),True,BLACK)
        #newTextRect = newText.get_rect()
        #newTextRect.topleft = (55 + (CELLSIZE * randX), 78 + (CELLSIZE * randY))
        
        nums.append([randAdd,randX,randY,])
        count += 1
    nums.append([random.randint(8,9), random.randint(4,14) ,random.randint(4,14)])
    nums.append([random.randint(5,6), random.randint(4,14) ,random.randint(4,14)])
    return nums

numsList = randomNumSpawn()
oneChosen = False

def numDetection():
    global addList
    for i in numsList:
            if(wormCoords.wormList[headIndex][x] == (i[1] * CELLSIZE)+50 and wormCoords.wormList[headIndex][y] == (i[2]*CELLSIZE)+75):
                    
                add1 = i[x]
                addList.append(add1)
                newHead = moveWorm()
                problemText = basicFont.render(" " + str(add1) , True, BLACK)
                windowSurface.blit(problemText,problemRect)
                wormCoords.wormList.insert(0, newHead)    
                del numsList[numsList.index(i)]
                
    
                       
  
                
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
    
    #Draws Numbers
    for i in numsList:
        randAdd = i[0]
        numPosX = i[1]
        numPosY = i[2]
        
        newText = numFont.render(str(randAdd),True,BLACK)
        newTextRect = newText.get_rect()
        topLeftX = 55 + (CELLSIZE * numPosX)
        topLeftY = 77 + (CELLSIZE * numPosY)
        newTextRect.topleft = (topLeftX,topLeftY)
        windowSurface.blit(newText,newTextRect)
    
    #FIX THE AUTO ALGORITHM
    
    #addList = [randAdd1,randAdd2,randX1,randY1,randX2,randY2]
    '''
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
    ''' 
        

def fillNum1(num):
    problemText = basicFont.render("__ +  " + str(num)  + "   ",True,BLACK)
    problemRect = problemText.get_rect()
    problemRect.topleft = (WINDOWWIDTH/2-100,10)
    windowSurface.blit(problemText,problemRect)
    
def fillNum2(num):
    problemText = basicFont.render(" " +num + "     ",True,BLACK)
    problemRect = problemText.get_rect()
    problemRect.topleft = (WINDOWWIDTH/2-100,10)
    windowSurface.blit(problemText,problemRect)

            
    
def drawWorm():
    print(wormCoords.wormList)
    for i in wormCoords.wormList:
        
        iRect = (i[x],i[y],CELLSIZE,CELLSIZE)
        pygame.draw.rect(windowSurface,GREEN,iRect)
    for i in wormCoords.wormList:
        iRect = (i[x] + CELLSIZE / 2,i[y] + CELLSIZE / 2,CELLSIZE / 4,CELLSIZE / 4)
        pygame.draw.rect(windowSurface,BLACK,iRect)
    
'''        
def moveWorm():
    print(wormCoords.wormList)
    delPos = len(wormCoords.wormList)-1
    del wormCoords.wormList[delPos]
    if wormDir == RIGHT:
        newHead = [wormCoords.wormList[0][x], wormCoords.wormList[0][y]]
    elif wormDir == LEFT:
        newHead = [wormCoords.wormList[0][x] - CELLSIZE,wormCoords.wormList[0][y]]
    elif wormDir == UP:
        newHead = [wormCoords.wormList[0][x],wormCoords.wormList[0][y] - CELLSIZE]
    elif wormDir == DOWN:
        newHead = [wormCoords.wormList[0][x],wormCoords.wormList[0][y] + CELLSIZE]
    if numDetection:
        return newHead
'''
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
    
    return newHead
    
wormCoords.getRandomHead()        
    
    

   
def checkForDeath():
    if wormCoords.wormList[headIndex][x] > ((CELLROW*CELLSIZE)):
        return True
    elif wormCoords.wormList[headIndex][y] > (30 + (CELLCOL*CELLSIZE)):
        return True
    elif wormCoords.wormList[headIndex][x] < (75):
        return True
    elif wormCoords.wormList[headIndex][y] < (95):
        return True
    else:
        return False
    count = 1
    while count < len(wormCoords.wormList - 1):
        if wormCoords.wormList[0][x] == wormCoords.wormList[count][x] and wormCoords.wormList[0][y] == wormCoords.wormList[count][y]:
            return True
        count+=1
    

def getAutoMatch():
    randAdd1 = random.randint(5,9)
    randAdd2 = sumNum - randAdd1
    randX1 = random.randint(1,14)
    randY1 = random.randint(1,14)
    randX2 = random.randint(1,14)
    randY2 = random.randint(1,14)
    '''
    addList = [randAdd1,randAdd2,randX1,randY1,randX2,randY2]
    numsList.append([randAdd1,randX1,randY1])
    numsList.append([randAdd2,randX2,randY2])
    return addList
    '''
perfectMatchList = getAutoMatch()

def winOrLose():
    print("WIn")
    print(add1+add2)
    if add1 + add2 == sumNum:
        
        winner = numFont.render("Kids Learn. They LearnByWorm",True,BLACK)
        winnerRect = footer.get_rect()
        winnerRect.topleft = (15,WINDOWHEIGHT-20)
        windowSurface.blit(winner,winnerRect)
def startScreen():
    windowSurface.fill(RED)
    startText = startFont.render("LearnByWorm",True, BLACK)
    startRect = startText.get_rect()
    startRect.topleft = (100,50)
    
startScreen()
windowSurface.fill(BLUE)

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
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
        break
    newHead = 0
    numDetection()
    moveWorm()
    #NO CHECKING IF ANSWERS ARE RIGHT
    #NO CORRECT TEXT DISPLAY
    add1 = addList[0]
    add2 = addList[1]
    mockSum = add1 + add2
    
    windowSurface.blit(problemText,problemRect)
    #wormCoords.wormList.insert(0, moveWorm() )
    drawFloor()
    drawWorm()
    #fillNum1(numsDet[0])
    #fillNum2(numsDet[1])
    pygame.display.update()
    FPSCLOCK.tick(FPS)
#GAME EXITS AND STARTS ABRUPTLY
winOrLose()
