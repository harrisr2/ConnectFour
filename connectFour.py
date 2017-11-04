'''Final Project - Connect Four
Features a graphic interfaces and various levels of computer strategies 
'''

import graphics
import random

#Functions to play and draw the game
def playConnectFour():
    '''Constructor that initializes the window and game gameBoard 
    for gameplay and difficulty'''
    gameWin = graphics.GraphWin("Connect Four Game", 1000, 650)
    gameWin.setCoords(0, 0, 1000, 650)
    back = graphics.color_rgb(255,255,224)
    gameWin.setBackground(back)
    locationDifficulty =opening(gameWin)
    location=locationDifficulty[0]
    difficulty=locationDifficulty[1]
    strategy = ComputerStrategy(difficulty)
    gameBoard = Board()
    gamePlay(gameWin,location, gameBoard, difficulty,strategy)
    playAgain(gameWin,gameBoard)

def opening(gameWin):
    '''Creates the opening sequence to the game where players choose
    a difficulty setting and background for playing
    Parameter:
    gameWin - window the graphic is drawn into'''
    welcome = graphics.Text(graphics.Point(500, 550), 
                            'WELCOME TO CONNECT FOUR!!!')
    welcome.setStyle('bold')
    welcome.setFace('arial')
    welcome.setSize(36)
    welcome.setTextColor('Midnight Blue')
    welcome.draw(gameWin)
    choice1 = graphics.Text(graphics.Point(500, 450), 
                            'Select Where You Would Like To Play!')
    choice1.setFace('arial')
    choice1.setSize(20)
    choice1.setTextColor('Midnight Blue')
    choice1.draw(gameWin)

    #chooses a place screen
    saylesBack = graphics.Rectangle(graphics.Point(675,100), 
                                    graphics.Point(970, 325))
    saylesBack.setFill('black')
    saylesBack.draw(gameWin)
    saylesBox=graphics.Image(graphics.Point(822.5,212.5),"saylesTN.gif")
    saylesBox.draw(gameWin)
    saylesText = graphics.Text(graphics.Point(822.5,212.5), 'Sayles')
    saylesText.setFace('arial')
    saylesText.setSize(30)
    saylesText.setStyle("bold")
    saylesText.setTextColor("white")
    saylesText.draw(gameWin)

    cmcBack = graphics.Rectangle(graphics.Point(30,100), 
                                 graphics.Point(325, 325))
    cmcBack.setFill('black')
    cmcBack.draw(gameWin)
    cmcBox=graphics.Image(graphics.Point(177.5,212.5),"cmcTN.gif")
    cmcBox.draw(gameWin)
    cmcText = graphics.Text(graphics.Point(177.5,212.5), 'CMC')
    cmcText.setFace('arial')
    cmcText.setSize(30)
    cmcText.setStyle("bold")
    cmcText.setTextColor("white")
    cmcText.draw(gameWin)

    bsBack = graphics.Rectangle(graphics.Point(347.5,100), 
                                graphics.Point(652.5, 325))
    bsBack.setFill('black')
    bsBack.draw(gameWin)
    baldBox=graphics.Image(graphics.Point(500,212.5),"baldTN.gif")
    baldBox.draw(gameWin)
    baldText = graphics.Text(graphics.Point(500,212.5), 'Bald Spot')
    baldText.setFace('arial')
    baldText.setSize(30)
    baldText.setStyle("bold")
    baldText.setTextColor("white")
    baldText.draw(gameWin)

    location=getBackground(gameWin)

    baldText.undraw()
    baldBox.undraw()
    bsBack.undraw()
    cmcText.undraw()
    cmcBox.undraw()
    cmcBack.undraw()
    saylesText.undraw()
    saylesBox.undraw()
    saylesBack.undraw()
    choice1.undraw()

    #Chooses a difficulty screen
    choice2 = graphics.Text(graphics.Point(500, 450), 
                            'Select A Difficulty Level! \n \n  Human Player Will Play First')
    choice2.setFace('arial')
    choice2.setSize(18)
    choice2.setTextColor('Midnight Blue')
    choice2.draw(gameWin)

    easy = graphics.Rectangle(graphics.Point(250,325),graphics.Point(490,275))
    easy.setFill('green')
    easyText = graphics.Text(graphics.Point(370,300),"EASY")
    easyText.setFace('arial')
    easyText.setSize(24)
    easyText.setTextColor("White")
    easy.draw(gameWin)
    easyText.draw(gameWin)

    medium = graphics.Rectangle(graphics.Point(510,325),graphics.Point(750,275))
    medium.setFill('gold')
    mediumText = graphics.Text(graphics.Point(630,300),"MEDIUM")
    mediumText.setFace('arial')
    mediumText.setSize(24)
    mediumText.setTextColor("White")
    medium.draw(gameWin)
    mediumText.draw(gameWin)

    advanced = graphics.Rectangle(graphics.Point(510,265),graphics.Point(750,215))
    advanced.setFill('black')
    advancedText = graphics.Text(graphics.Point(630,240),"ADVANCED")
    advancedText.setFace('arial')
    advancedText.setSize(24)
    advancedText.setTextColor("White")
    advanced.draw(gameWin)
    advancedText.draw(gameWin)

    hard = graphics.Rectangle(graphics.Point(250,265),graphics.Point(490,215))
    hard.setFill('red')
    hardText = graphics.Text(graphics.Point(370,240),"HARD")
    hardText.setFace('arial')
    hardText.setSize(24)
    hardText.setTextColor("White")
    hard.draw(gameWin)
    hardText.draw(gameWin)

    difficulty = getDifficulty(gameWin)
    return [location,difficulty]

def gamePlay(gameWin,location, gameBoard, difficulty,strategy):
    '''Draws the gameBoard for Connect Four in the location chosen by the player
    Parameter:
    gameWin - window the graphic is drawn into
    location - image file of the location chosen by the player
    gameBoard - list of lists containing pieces 
    difficulty - the click of the user used to pick strategy
    strategy - the computer's way of choosing where to put a piece
    '''
    gamePlace = graphics.Image(graphics.Point(500,325), location)
    gamePlace.draw(gameWin)
    grid=graphics.Image(graphics.Point(500,300),"CFBoard.gif")
    grid.draw(gameWin)
    getFour=False
    turnCount=0
    while getFour==False:
        if turnCount%2==0:
            playerColor="maize"
            setColumn = getHumanColumn(gameWin)
        else:
            playerColor="blue"
            if strategy.strategyReturn() == "easy":
                setColumn = strategy.easy()
            if strategy.strategyReturn() == "medium":
                setColumn = strategy.medium(gameBoard)
            if strategy.strategyReturn() == "hard":
                setColumn = strategy.hard(gameBoard)
            if strategy.strategyReturn() == "advanced":
                setColumn = strategy.advanced(gameBoard)
        filledSpot=gameBoard.getTileCoordinate(setColumn,playerColor)
        gameBoard.playTile(filledSpot,playerColor)
        tileFall(gameWin,filledSpot,playerColor)
        end=gameBoard.checkForWin()
        if end=="win":
            drawWin(gameWin)
            getFour=True  
        elif end =="loss":
            drawLoss(gameWin)
            getFour=True
        elif end == "tie":
            drawTie(gameWin)
            getFour = True
        else:
            turnCount+=1
    gameWin.getMouse()

def getBackground(gameWin):
    """Determines desired background for game based on clicks by user
    Parameter:
    gameWin - window the graphic is drawn into"""
    back = False
    while back ==False:
        userClick=gameWin.getMouse()
        if int(userClick.getX()) in range(675,970) and int(userClick.getY()) in range(100,325):
            image = "sayles.gif"
            back=True
            return image
        elif int(userClick.getX()) in range(30,325) and int(userClick.getY()) in range(100,325):
            image= "cmc.gif"
            back=True
            return image
        elif int(userClick.getX()) in range(348,653) and int(userClick.getY()) in range(100,325):
            image = "bald.gif"
            back=True
            return image      
        
def getDifficulty(gameWin):
    """Determines desired difficulty of game, given graphical user input
    Parameter:
    gameWin - window the graphic is drawn into
    """
    userClick=gameWin.getMouse()
    if int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(275,325):
        difficulty = 1 #makes easy
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(275,325):
        difficulty = 2 #makes medium
    elif int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(215,265):
        difficulty = 3 #makes hard
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(215,265):
        difficulty = 4 #make advanced 
    else:
        difficulty=getDifficulty(gameWin)
    return difficulty
        
def getHumanColumn(gameWin):
    """This function returns the column selected by the human player
    through clicks
    Parameter:
    gameWin - window the graphic is drawn into
    """
    userClick = gameWin.getMouse()
    if int(userClick.getX()) in range(190,265):
        setColumn = 0
    elif int(userClick.getX()) in range(275,355):
        setColumn = 1
    elif int(userClick.getX()) in range(370,445):
        setColumn=2
    elif int(userClick.getX()) in range(455,535):
        setColumn=3
    elif int(userClick.getX()) in range(555,625):
        setColumn=4
    elif int(userClick.getX()) in range(635,715):
        setColumn=5
    elif int(userClick.getX()) in range(725,805):
        setColumn=6
    else:
        setColumn=getHumanColumn(gameWin)
    return setColumn

def tileFall(gameWin, coordinate, playerColor):
    '''This function animates the tile fall through the gameBoard
    Parameters:
    gameWin - window the graphic is drawn into
    coordinate - the location of the tiles placement
    playerColor - the color of the tile
    '''
    if int(coordinate[0])==0:
        xCoord=224
    if int(coordinate[0])==1:
        xCoord=314
    if int(coordinate[0])==2:
        xCoord=404
    if int(coordinate[0])==3:
        xCoord=494
    if int(coordinate[0])==4:
        xCoord=586
    if int(coordinate[0])==5:
        xCoord=675
    if int(coordinate[0])==6:
        xCoord=766
    if coordinate[1]==5:
        yCoord=80
    if coordinate[1]==4:
        yCoord=170
    if coordinate[1]==3:
        yCoord=260
    if coordinate[1]==2:
        yCoord=350
    if coordinate[1]==1:
        yCoord=440
    if coordinate[1]==0:
        yCoord=530
    if playerColor=="maize":
        color="gold"
    elif playerColor=="blue":
        color="blue"
    playerPiece = graphics.Circle(graphics.Point(xCoord,600),38)
    i=0
    #makes sure piece begins animating at the top of the gameBoard
    if yCoord < 500: 
        while (600-i) > yCoord +100:
            i += 20 #animates piece
            #playerPiece.undraw()
            playerPiece=graphics.Circle(graphics.Point(xCoord,600-i),38)
            playerPiece.setFill(color)
            playerPiece.draw(gameWin)
            playerPiece.undraw()
    playerPiece = graphics.Circle(graphics.Point(xCoord,yCoord),38)
    playerPiece.setFill(color)
    playerPiece.draw(gameWin)

def drawWin(gameWin):
    '''Draws stars all over the screen to indicate a win by the user
    Parameter:
    gameWin - window the graphic is drawn into
    '''
    for i in range (0, 1200, 100):
        for j in range(0, 800, 100):
            winStar = graphics.Image(graphics.Point(i, j),"goldstar.gif")
            winStar.draw(gameWin)
    finalStar = graphics.Image(graphics.Point(500,325),"goldstar.gif")
    finalStar.draw(gameWin)
    winText = graphics.Text(graphics.Point(500, 325), "YOU WIN!")
    winText.setFace("arial")
    winText.setStyle('bold')
    winText.setSize(36)
    winText.draw(gameWin)

def drawLoss(gameWin): 
    '''Draws sad faces to indicate a loss by the user all over the 
    screen
    Parameter:
    gameWin - window the graphic is drawn into
    '''
    for i in range (0, 1200, 100):
         for j in range(0, 800, 100):
            loseFace = graphics.Image(graphics.Point(i, j),"lose.gif")
            loseFace.draw(gameWin)
    finalLose = graphics.Circle(graphics.Point(500,325),150)
    finalLose.setFill("blue")
    finalLose.draw(gameWin)
    loseText = graphics.Text(graphics.Point(500, 325), "Computer Wins")
    loseText.setFace("arial")
    loseText.setStyle('bold')
    loseText.setSize(36)
    loseText.draw(gameWin)

def drawTie(gameWin):
    '''Draws ties all over the screen to indicate it was a tie game
    also draws text
    Parameter:
    gameWin - window the graphic is drawn into
    '''
    for i in range (0, 1200, 100):
        for j in range(0, 800, 100):
            tie = graphics.Image(graphics.Point(i, j),"tie.gif")
            tie.draw(gameWin)
    finalTie = graphics.Image(graphics.Point(500,325),"finalTie.gif")
    finalTie.draw(gameWin)
    tieText = graphics.Text(graphics.Point(500, 250), "It's a tie!")
    tieText.setFace("arial")
    tieText.setStyle('bold')
    tieText.setSize(36)
    tieText.draw(gameWin)        

def playAgain(gameWin,gameBoard):
    '''Draws the buttons and texts to play the game again and takes the user clicks
    to indicate whether to open a new window and run the module again or
    to close the window
    Parameter:
    gameWin - window the graphic is drawn into
    gameBoard - needs to be reset in order to play the game again
    '''
    backColor = graphics.color_rgb(255,255,224)
    back = graphics.Rectangle(graphics.Point(0,0),graphics.Point(1000,650))
    back.setFill(backColor)
    back.draw(gameWin)
    replay = graphics.Text(graphics.Point(500,550),"Would you like to play again?")
    replay.setStyle('bold')
    replay.setFace('arial')
    replay.setSize(36)
    replay.setTextColor('Midnight Blue')
    replay.draw(gameWin)
    yes = graphics.Rectangle(graphics.Point(250,325),graphics.Point(490,275))
    yes.setFill('green')
    yesText = graphics.Text(graphics.Point(370,300),"YES")
    yesText.setFace('arial')
    yesText.setSize(24)
    yesText.setTextColor("White")
    yes.draw(gameWin)
    yesText.draw(gameWin)
    no = graphics.Rectangle(graphics.Point(510,325),graphics.Point(750,275))
    no.setFill('gray')
    noText = graphics.Text(graphics.Point(630,300),"NO")
    noText.setFace('arial')
    noText.setSize(24)
    noText.setTextColor("White")
    no.draw(gameWin)
    noText.draw(gameWin)
    userClick=gameWin.getMouse()
    if int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(275,325):
        gameBoard.resetBoard()
        playConnectFour()
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(275,325):
        return


class Board:
    '''This class will contain the gameBoard for Connect Four
    and functions that find coordinates and indexes for 
    the pieces on the gameBoard. Also this class contains
    functions which put tiles on the gameBoard and check if
    there are four in a row on the gameBoard'''
    def __init__(self,board=[['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],
                      ['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],
                      ['.','.','.','.','.','.']]):
        '''Parameter:
        board - list of lists indicating the columns and rows, 
        outer list is columns, inner list is rows
        '''
        self.gameBoard = board
    
    def resetBoard(self):
        '''Resets the board back to empty so that the user can 
        play the game again'''
        for item in self.getGameBoard():
            for i in range(6):
                item[i] = "."
        
    def getGameBoard(self):
        '''Returns the gameBoard, which is a list of lists indicating
        the pieces and positions'''
        return self.gameBoard
        
    def getColumn(self, dictionary):
        '''Returns the list of the column indicated by column Number
        Parameters:
        colNum - a string that indicates col and then the number,
        ex.col1 or col2
        dictionary - dictionary containing rows and cols as lists
        '''
        #the outer list of the board is columns
        if "." in self.gameBoard[0]:
            dictionary["col0"] = self.gameBoard[0]
        if "." in self.gameBoard[1]:
            dictionary["col1"] = self.gameBoard[1]
        if "." in self.gameBoard[2]:
            dictionary["col2"] = self.gameBoard[2]
        if "." in self.gameBoard[3]:
            dictionary["col3"] = self.gameBoard[3]
        if "." in self.gameBoard[4]:
            dictionary["col4"] = self.gameBoard[4]
        if "." in self.gameBoard[5]:
            dictionary["col5"] = self.gameBoard[5]
        if "." in self.gameBoard[6]:
            dictionary["col6"] = self.gameBoard[6]
    
    def getRow(self, dictionary):
        '''Returns the list of the row indiciated by rowNum
        Parameters:
        rowNum - a string that indicates row and then the number,
        ex.row1 or row3
        dictionary - dictionary containing rows and cols as lists
        '''
        #the inner list of the board is rows, thus you need the for loops
        rowList0 = []
        for i in range(0,7): #makes list for row 0
            rowList0.append(self.gameBoard[i][0])
        dictionary["row0"] = rowList0
        rowList1=[]
        for i in range(0,7): #makes list for row 1
            rowList1.append(self.gameBoard[i][1])
        dictionary["row1"] = rowList1
        rowList2=[]
        for i in range(0,7): #makes list for row 2
            rowList2.append(self.gameBoard[i][2])
        dictionary["row2"] = rowList2
        rowList3=[]
        for i in range(0,7):  #makes list for row 3
            rowList3.append(self.gameBoard[i][3])
        dictionary["row3"] = rowList3
        rowList4=[]
        for i in range(0,7): #makes list for row 4
            rowList4.append(self.gameBoard[i][4])
        dictionary["row4"] = rowList4
        rowList5=[]
        for i in range(0,7): #makes list for row 5
            rowList5.append(self.gameBoard[i][5])
        dictionary["row5"] = rowList5
        
    def getDiagonal(self, dictionary):
        '''Creates a dictionary where the first diagonal is
        the top left corner, moving over by column
        each time. 
        Parameters:
        dictionary - keys of diagNums and values of what is in spaces
        '''
        # the keys for this are numbers, starting at the bottom left of the gameBoard 
        #row & col numbers begin at top left corner 
        #rows go from 0 to 5
        #cols go from 0 to 6
        acc = 0 # this wil change the diag number each time 
        for i in range(5, -1, -1): #row for loop beginning at 5th row
            currentDiag1 = []
            col = 0
            n = i
            while n < 6 and n >= 0: #n is row beginning at i
                tile = self.gameBoard[col][n]
                currentDiag1.append(tile)
                col+=1 # moves over the columns to the right 
                n+=1 #moves through rows downward
            dictionary["diag"+str(acc)] = currentDiag1  
            acc += 1
            currentDiag2 = []
            col= 0
            m = i
            while m < 6 and m > -1: #m is row beginning at i
                tile = self.gameBoard[col][m]
                currentDiag2.append(tile)
                col+=1 # moves over the columns to the right 
                m-=1 #moves through rows upwards
            dictionary["diag"+str(acc)] = currentDiag2
            acc+=1
        for i in range(0, 7, 1): #col is i, starts at top left moves right 
            currentDiag3 = []
            row = 0 #starts at row 0, top of board
            p = i
            while p < 7 and p > -1 and row < 6: #p is column 
                tile = self.gameBoard[p][row]
                currentDiag3.append(tile)
                row+=1 #moves down the rows
                p+=1 #moves across the columns
            dictionary["diag"+str(acc)] = currentDiag3
            acc+=1
            currentDiag4 = []
            row = 5 # starts at row 5, bottom of board
            q = i
            while q < 7 and q > -1 and row < 6: #q is column
                tile = self.gameBoard[q][row]
                currentDiag4.append(tile)
                row-=1 #moves up the rows
                q+=1 #moves right acorss the columns
            dictionary["diag"+str(acc)] = currentDiag4
            acc += 1
    
    def getTileCoordinate(self, setColumn, playerColor):
        """This function finds the row that the tile will fall to when a column
        is selected.  If there is no available row, it asks for another input.
        Parameters:
        setColumn - the input given by either the human or the computer
        playerColor - the tile color of the current player
        difficulty - the difficulty of the computer strategy
        """
        originalColumn = setColumn
        for i in range(6):
            #when there is a filled spot in the column
            if self.gameBoard[int(setColumn)][i]=="blue" or self.gameBoard[int(setColumn)][i]=="maize":
                #if there is an empty spot above it
                if (i-1)<0 and playerColor=="maize":
                    while setColumn == originalColumn:
                        setColumn = getHumanColumn(gameWin)
                elif (i-1)<0 and playerColor=="blue":
                    while setColumn == originalColumn:
                        for k in range(7):
                            if self.gameBoard[k][0] == '.':
                                setColumn = k      
                #return the coordinate of the first available row in the column
                else:
                    coordinate=(setColumn,i-1)
                    return coordinate
            elif self.gameBoard[setColumn]==[".",".",".",".",".","."]:
                coordinate=(setColumn,5)
                return coordinate
    
    def playTile(self, coordinate, playerColor):
        """Changes the value of the first available space in a column to 
        the color of the current player.
        Parameters:
        coordinate - the place that the tile will be
        playerColor - the color of the tile that will be placed
        """
        #sets the value at gameBoard in the correct column and row to either
        #"maize" or "blue" according to playerColor
        firstIndex=coordinate[0]
        secondIndex=coordinate[1]
        self.gameBoard[int(firstIndex)][int(secondIndex)]=playerColor
    
    def checkForWin(self):
        """Creates a dictionary of rows, columns, and diagonals to check
        if there are four of the same color anywhere. Returns whether
        the user has lost of won the game."""
        dictionary={}
        self.getRow(dictionary)
        self.getColumn(dictionary)
        self.getDiagonal(dictionary)
        full = 'complete'
        while full == 'complete': #if the game is full, the game is a tie
            for column in self.gameBoard:
                for piece in column:
                    if piece == '.':
                        full = 'notComplete'
            if full == 'complete':
                return "tie" 
        for key in dictionary:
            winList=[]
            if len(dictionary[key])>=4: # if the length of the diagonal is at least four 
                for place in dictionary[key]:
                    if len(winList)==0: #creates list to count up to four of the pieces
                        winList.append(place)
                    else:
                        if winList[0]==place:
                            winList.append(place)
                        elif winList[0]!=place:
                            winList=[]
                            winList.append(place)
                    if len(winList)==4 and winList[0] == 'maize' and winList[3] =="maize":
                        return "win" #user wins the game
                    elif len(winList)==4 and winList[0]=="blue" and winList[3] == 'blue':
                        return "loss" #user loses the game
        return False
    
    
class ComputerStrategy:
    '''This class contains the AI component of the game, 
    the computer will have various strategies created 
    within this class including easy, medium, hard, and
    advanced level startegies. For the strategies to function
    the input utilizes getColumnFromDictionary function to figure out
    where to play its pieces'''
    def __init__(self, difficulty):
        '''Sets the strategy for the computer player
        Parameter:
        gameBoard - contains location of pieces 
        difficulty - the level of the computer chosen by user
        '''
        if difficulty==1: #easy
            self.strategy = "easy"
        elif difficulty == 2: #medium
            self.strategy = "medium"
        elif difficulty == 3: #hard
            self.strategy  = "hard"
        elif difficulty == 4: #advanced
            self.strategy = "advanced"
    
    def strategyReturn(self):
        '''Returns the strategy that was selected by the user
        choice of difficulty'''
        return self.strategy

    def easy(self):
        '''Returns the column selected by the easy strategy 
        the column is selected randomly making the game easy to beat'''
        setColumn = random.randint(0,6)
        return setColumn
    
    def medium(self, gameBoard):
        '''Returns the column for strategy and placement of piece.
        This stategy is more difficult than easy and thus is a medium
        level player. 
        Parameter:
        gameBoard - location of pieces
        '''
        dictionary ={}
        gameBoard.getRow(dictionary)
        gameBoard.getColumn(dictionary)
        longest = []#longest chain of desired color so far
        setColumn = -1
        for key in dictionary:
            checkList=[]#to build a list of longest of desired color for given key
            for place in dictionary[key]: # place is blue maize or . 
                if place==".":
                    checkList=[]
                elif place=="maize":
                    checkList=[]
                elif len(checkList)==0:
                    checkList.append(place) #place will be blue
                else:
                    if checkList[0]==place:#append to checkList if matching
                        checkList.append(place)
                if len(checkList) > len(longest) and place!=".":
                    longest = checkList[:]#copy checklist to longest
                    desiredKey = key #dict key containing current longest matches
                    index = dictionary[desiredKey].index(place) #the space of first item in list
                    if dictionary[desiredKey][index-1] == ".": #keeps from playing in filled spot
                        if len(longest) == 1 and index-4 >= 0: #keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        elif len(longest) == 2 and index-3 >=0:#keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        elif index-2>=0:#keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
        if setColumn not in range(0,7):# if none of the above conditions were true, play a random place
            setColumn = random.randint(0,6)
        return setColumn 
    
        
    def hard(self, gameBoard):
        '''Returns the column for which the computer will play using 
        a hard strategy to beat. 
        Parameter:
        gameBoard - list of lists that has pieces and locations
        '''
        firstMove = 0
        for item in gameBoard.getGameBoard():#checks items in the list of spaces in the board
            firstMove += item.count("maize") #adds the number of times that maize is present
        if firstMove == 1:#if only one maize on the board
            maize = -1
            while maize == -1:
                for item in gameBoard.getGameBoard():#checks items in the list of spaces in the board
                    if "maize" in item:
                        firstPiece=gameBoard.getGameBoard().index(item)#get the index of maize piece
                        maize = 0
            if firstPiece - 1>=0:#if index of maize is not 0
                setColumn = firstPiece - 1 #place the piece to the left of the maize piece to block row attempt
                return setColumn
        dictionary ={}
        gameBoard.getRow(dictionary)
        gameBoard.getColumn(dictionary)
        longest = []#longest chain of desired color so far
        setColumn = -1
        for key in dictionary:
            checkList=[]#to build a list of longest of desired color for given key
            for place in dictionary[key]: #blue maize or .
                if len(longest) == 3:
                    index = dictionary[desiredKey].index('maize')
                    if index-1>=0:
                        if dictionary[desiredKey][index-1] == ".":
                            setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                elif place==".":
                    checklist=[]
                elif place=="blue":
                    checklist=[]
                elif len(checkList)==0:
                    checkList.append(place)
                else:
                    if checkList[0]==place:#append to checkList if matching
                        checkList.append(place)
                if len(checkList) > len(longest) and place!=".":
                    longest = checkList[:]#copy checklist to longest
                    desiredKey = key#dict key containing current longest matches
                    index = dictionary[desiredKey].index(place)#the space of first item in list
                    setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                    if dictionary[desiredKey][index-1] == ".": #keeps from playing in filled spot
                        if len(longest) == 1 and index-4 >= 0: #keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        elif len(longest) == 2 and index-3 >=0:#keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        elif index-2>=0:#keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                if "maize" in longest and "row" in key:
                    firstMaizeInRow = dictionary[desiredKey].index("maize")
                    numMaizeInRow = len(longest)
                    checkBlue = -1
                    checkBalnk = -1
                    if firstMaizeInRow-1>=0:# makes sure its still in range 
                        checkBlue = dictionary[desiredKey][firstMaizeInRow-1]
                    if firstMaizeInRow +numMaizeInRow <= 6:# makes sure its still in range 
                        checkBlank = dictionary[desiredKey][firstMaizeInRow+numMaizeInRow]
                    if checkBlue == "blue":
                        setColumn = self.getColumnFromDictionary(firstMaizeInRow+numMaizeInRow+1,gameBoard,desiredKey,dictionary)
        if setColumn not in range(0,7):
            setColumn = random.randint(0,6)
        return setColumn 
        
    def advanced(self, gameBoard):
        '''Returns the column for strategy and placement of piece
        with an advanced strategy.
        Parameter:
        gameBoard - location of pieces
        '''
        firstMove = 0
        for item in gameBoard.getGameBoard():
            firstMove += item.count("maize")
        if firstMove == 1: # this makes sure it plays a piece next to the user's piece
            maize = False
            while maize == False:
                for item in gameBoard.getGameBoard():
                    if "maize" in item:
                        firstPiece=gameBoard.getGameBoard().index(item)
                        maize = True
            if firstPiece - 1 >= 0: #if there is a column to the left of the user piece 
                setColumn = firstPiece - 1
                return setColumn
        dictionary ={}
        gameBoard.getRow(dictionary)
        gameBoard.getColumn(dictionary)
        #longest chain of desired color so far
        longest = []
        setColumn = -1
        while setColumn ==-1:
            for key in dictionary:
                #to build a list of longest of desired color for given key
                checkList=[]
                #a win could theoretically occur here
                if len(dictionary[key])>=4:
                    for place in dictionary[key]: #blue maize or . i
                        if len(longest) == 3:
                            index = dictionary[desiredKey].index(longest[0])
                            if index-1>=0:
                                if dictionary[desiredKey][index-1] == ".":
                                    setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        if place==".":
                            checklist=[]
                        elif len(checkList)==0:
                            checkList.append(place)
                        else:
                            #append to checkList if matching
                            if checkList[0]==place:
                                checkList.append(place)
                            if checkList[0]!= place:
                                checkList= []
                                checkList.append(place)
                        if len(checkList) > len(longest):
                            longest = checkList
                            desiredKey = key
                            index = dictionary[desiredKey].index(place)
                            if dictionary[desiredKey][index-1] == ".": #keeps from playing in filled spot
                                if len(longest) == 1 and index-4 >= 0: #keeps from playing in useless spot
                                    setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                                elif len(longest) == 2 and index-3 >=0:#keeps from playing in useless spot
                                    setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                                elif index-2>=0:#keeps from playing in useless spot
                                    setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        if "blue" in longest and len(longest)==3 and "row" in key:
                            firstBlueInRow = dictionary[desiredKey].index("blue")
                            numBlueInRow = len(longest)
                            checkLeft = -1
                            checkRight = -1
                            if firstBlueInRow-1>= 0: #makes sure its still in range 
                                checkLeft = dictionary[desiredKey][firstBlueInRow-1]
                            if firstBlueInRow +numBlueInRow <= 6: #makes sure its still in range 
                                checkRight = dictionary[desiredKey][firstBlueInRow+numBlueInRow]
                            if checkLeft == ".":
                                setColumn = self.getColumnFromDictionary(firstBlueInRow,gameBoard,desiredKey,dictionary)
                            if checkRight == ".":
                                setColumn = self.getColumnFromDictionary(firstBlueInRow+numMaizeInRow+1,gameBoard,desiredKey,dictionary)
                        if "maize" in longest and "row" in key and len(longest)>=2:
                            checkBlue = -1
                            checkBlank = -1
                            firstMaizeInRow = dictionary[desiredKey].index("maize")
                            numMaizeInRow = len(longest)
                            if firstMaizeInRow-1>=0: # makes sure its still in range 
                                checkBlue = dictionary[desiredKey][firstMaizeInRow-1]
                            if firstMaizeInRow +numMaizeInRow <= 6: #makes sure its still in range
                                checkBlank = dictionary[desiredKey][firstMaizeInRow+numMaizeInRow]
                            if checkBlue == "blue":
                                setColumn = self.getColumnFromDictionary(firstMaizeInRow+numMaizeInRow+1,gameBoard,desiredKey,dictionary)
                if setColumn not in range(0,7):# this will allow strategy to play a random column
                    setColumn = random.randint(0,6)
        return setColumn 
        

    def getColumnFromDictionary(self, index, gameBoard, desiredKey, dictionary):
        '''Returns a column on the gameBoard from the dictionary
        Parameter:
        index - place in list to place piece
        gameBoard - location of pieces
        desiredKey - column, row, or diagonal indicator
        dictionary - contains all lists of pieces
        '''
        setColumn = None
        if 'col' in desiredKey:#if it is a column
            setColumn = int(desiredKey[3])#third item in column key is the int of column
            return setColumn
        elif 'row' in desiredKey:#if it is a row
            rowNum = int(desiredKey[3])#third item in row key is the int of the row
            if rowNum<5:#if not the last row
                if index-1 in range (0,6):#if not the first column
                    rowDown = dictionary["row"+str(rowNum+1)][index-1]#go one row down and one column to the left
                    if rowDown == ".":#if that space is empty
                        setColumn = random.randint(0,6)#just play randomly, playing there doesn't advance the goal
                    else:
                        setColumn = index-1#the spaces are filled up to the place you want to play, advances goal
            elif index -1 >= 0: #if not the first column
                setColumn = index - 1   
            else:
                setColumn = index
            return setColumn
        
if __name__=="__main__":
    playConnectFour()
                         
