# -*- coding: utf-8 -*-
from graphics import *
import random 

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' '] * W for row in range(H) ]   
        self.initGraphicBoard(self.width, self.height) 
                    
    def __repr__(self):
        H = self.height
        W = self.width
        s = ''
        for row in range(0, H):
            s += '|'   
            for col in range(0, W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2 * W + 1) * '-'
        
        s += '\n'
        
        for col in range(0, W):
            if col >= 10:
                col = col % 10
            s += ' ' + str(col)
        
        return s
    
    
    def addMove(self, col, ox):
        row = self.height - 1
        
        while row >= 0:
            if self.data[row][col] == ' ':
                
                if ox is 'O':
                    self.graphical_data[row][col].setFill("blue")
                    self.graphical_data[row][col].setOutline("blue")
                else:
                    self.graphical_data[row][col].setFill("red")
                    self.graphical_data[row][col].setOutline("red")
                    
                self.data[row][col] = ox
                break
            else:
                row -= 1
                
                
    def clear(self):
        W = self.width
        H = self.height
        self.data = [ [' '] * W for row in range(H) ]
                
        
    def setBoard(self, moveString):
        nextCh = 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width - 1:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            
            
    def allowsMove(self, c):
        H = self.height
        W = self.width
        D = self.data
        
        if c < 0 or c > W - 1:
            return False
                
        for row in range(0, H):
                if D[row][c] == ' ':
                    return True
                
        return False
    
    
    def isFull(self):
        W = self.width
        isAllows = False
        
        for col in range(0, W):
            isAllows = self.allowsMove(col)
            if isAllows == True:
                return False
                
        return True
    
    
    def delMove(self, c):
        H = self.height
        row = 0
        
        while row < H:
            if self.data[row][c] != ' ':
                self.data[row][c] = ' '
                self.graphical_data[row][c].setFill(color_rgb(204, 204, 204))
                self.graphical_data[row][c].setOutline(color_rgb(204, 204, 204))
                break
            else:
                row += 1
    
                
    def winsFor(self, ox):
        H = self.height
        W = self.width
        D = self.data
        
        # horizontal check
        for row in range(0, H):
            for col in range(0, W - 3):
                if D[row][col] == ox and \
                   D[row][col + 1] == ox and \
                   D[row][col + 2] == ox and \
                   D[row][col + 3] == ox:
                    return True
                
        # vertical check       
        for row in range(0, H - 3):
            for col in range(0, W):
                if D[row][col] == ox and \
                   D[row + 1][col] == ox and \
                   D[row + 2][col] == ox and \
                   D[row + 3][col] == ox:
                    return True       
                 
        # diagonal leftDown to rightUp check        
        for row in range(0, H - 3):
            for col in range(3, W):
                if D[row][col] == ox and \
                   D[row + 1][col - 1] == ox and \
                   D[row + 2][col - 2] == ox and \
                   D[row + 3][col - 3] == ox:
                    return True
                
        # diagonal leftUp to rightDown check     
        for row in range(0, H - 3):
            for col in range(0, W - 3):
                if D[row][col] == ox and \
                   D[row + 1][col + 1] == ox and \
                   D[row + 2][col + 2] == ox and \
                   D[row + 3][col + 3] == ox:
                    return True
                
        return False
    

    def hostGame(self):
        print("Welcome to Connect Four!\n")
        print(self)
        
        isWins = False
        checker = 'X'
        
        while self.isFull() == False:            
            print("\n" + checker + "'s choice: "),
            users_col = self.getSelectedCol(self.win.getMouse().getX())
            print(str(users_col) + "\n")
            # users_col = input("\n" + checker + "'s choice: ")
            
            if self.allowsMove(users_col) == False:
                # print("Out of range. Points must be re-entered.\n")
                continue
            
            self.addMove(users_col, checker)            
            
            isWins = self.winsFor(checker)
            if isWins == True:
                self.win.close()
                print("\n" + checker + " wins -- Congratulations!\n")
                print(self)
                return
            
            print(self)
            
            checker = self.changeChecker(checker)
        
        self.win.close()
        print("\nDraw Game!\n")
        print(self)
        
        
    def initGraphicBoard(self, W, H):
        self.diameter = 60
        self.radius = self.diameter / 2
        diameter = self.diameter
        radius = self.radius
        self.win = GraphWin("Connect Four", (diameter * W) + diameter, (diameter * H) + diameter)
        self.win.setBackground(color_rgb(255, 161, 51))
        self.graphical_data = []
        for row in range(H):
            new_row = []
            for col in range(W):
                center = Point(diameter + (diameter * col), diameter + (diameter * row))
                circle = Circle(center, radius - 2)
                circle.setFill(color_rgb(204, 204, 204))
                circle.setOutline(color_rgb(204, 204, 204))
                circle.draw(self.win)
                new_row += [circle]
            self.graphical_data += [new_row]
            
            
    def getSelectedCol(self, pointX):
        diameter = self.diameter
        radius = self.radius
        width = self.width
        
        if pointX < radius:
            return -1
        
        if pointX > radius + (diameter * width):
            return width
        
        for devidedColumn in range(0, width):
                colCenterX = diameter + (diameter * devidedColumn)
                if colCenterX - radius <= pointX and pointX <= colCenterX + radius:
                    return devidedColumn


    def changeChecker(self, nextChecker):
        if nextChecker == 'X':
            return 'O'
        else:
            return 'X'
        
    def playGame(self, px, po, winCount):
        print("Welcome to Connect Four!\n")
        print(self)
        
        isWins = False
        checker = 'X'
        
        while self.isFull() == False:            
            print("\n" + checker + "'s choice:"),
            
            if checker is 'X':
                users_col = px.nextMove(b)
                # users_col = self.getSelectedCol(self.win.getMouse().getX())
            else:
                users_col = po.nextMove(b)
                # users_col = self.getSelectedCol(self.win.getMouse().getX())
                
            print(str(users_col) + "\n")
            
            if self.allowsMove(users_col) == False:
                continue
            
            self.addMove(users_col, checker)
            
            print(self)
            
            isWins = self.winsFor(checker)
            if isWins == True:
                if checker is 'O':
                    winCount.oWin()
                else:
                    winCount.xWin()

                self.win.close()
                print("\n" + checker + " wins!\n")
                return
            
            checker = self.changeChecker(checker)
        
        self.win.close()
        print("\nDraw Game!\n")
        print(self)

class Player_AI:
    
    def __init__(self, ox, tbt, ply):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s
    
    def oppCh(self):
        if self.ox is 'X':
            return 'O'
        else:
            return 'X'
        
    def scoreBoard(self, b):
        if b.winsFor(self.ox):
            return 100.0
        
        if b.winsFor(self.oppCh()):
            return 0.0
        
        return 50.0
    
    def tiebreakMove(self, scores):
        maxIndices = [i for i, x in enumerate(scores) if x == max(scores)]
        if self.tbt is "LEFT":
            return maxIndices[0]
        elif self.tbt is "RIGHT":
            return maxIndices[len(maxIndices) - 1]
        else:
            return random.choice(maxIndices)

    def scoresFor(self, b):
        W = b.width
        numericScores = [50.0] * W

        for index in range(W):
            if b.allowsMove(index) is False:
                numericScores[index] = -1.0
            elif self.ply is 0:
                numericScores[index] = self.scoreBoard4Tourney(b)
            elif b.winsFor(self.ox) or b.winsFor(self.oppCh()):
                numericScores[index] = self.scoreBoard4Tourney(b)
            else :
                b.isGraphicOn = False
                b.addMove(index, self.ox)
                opponent = Player_AI(self.oppCh(), "RANDOM", self.ply - 1)
                oppScore = opponent.scoresFor(b)
                oppMax = max(oppScore)
                if oppMax == -1.0 :
                    oppMax = 50.0
                numericScores[index] = 100 - oppMax;
                b.delMove(index)
                b.isGraphicOn = True
        return numericScores

    def nextMove(self, b):
        return self.tiebreakMove(self.scoresFor(b))
    
    """
    모바일테스트 개발팀 박명성, UIT 개발실 박지만 팀 Connect Four scoreBoard4Tourney(self, b) function comment
    기존 내가 이기는 경우 상대방이 이기는 경우 이외에
    
    1. 
    """
    def scoreBoard4Tourney(self, b):
        if b.winsFor(self.ox):
            return 100.0
        
        if b.winsFor(self.oppCh()):
            return 0.0
        
        if self.opp3RunCase(b) == 1:
            return 10.0
        elif self.opp3RunCase(b) == 2:
            return 30.0
        
        if self.self3RunCase(b) == 1:
            return 80.0
        elif self.self3RunCase(b) == 2:
            return 60.0        
        
        if self.self2RunCase(b):
            return 70.0
        
        return 50.0
    
    # opp three run case
    def opp3RunCase(self, b):
        D = b.data
        W = b.width
        H = b.height        
        
        # horizontal check
        for row in range(0, H - 1):
            for col in range(0, W - 3):
                if D[row][col] == self.oppCh() and \
                   D[row][col + 1] == self.oppCh() and \
                   D[row][col + 2] == self.oppCh():
                    if D[row + 1][col - 1] != ' ' and \
                       D[row + 1][col + 3] != ' ' and \
                       D[row][col - 1] == ' ' and \
                       D[row][col + 3] == ' ':
                        if col - 1 < 0 or col + 3 >= W:
                            return 2
                        return 1
                    
        # 1st floor    
        row = b.height - 1          
        for col in range(1, W - 3):
            if D[row][col] == self.oppCh()  and \
               D[row][col + 1] == self.oppCh()  and \
               D[row][col + 2] == self.oppCh():
                if D[row][col - 1] == ' ' and \
                   D[row][col + 3] == ' ':
                    if col - 1 < 0 or col + 3 >= W:
                        return 2
                    return 1
                 
        # diagonal leftDown to rightUp check
        for row in range(0, H - 2):
            for col in range(2, W):
                if D[row][col] == self.oppCh() and \
                   D[row + 1][col - 1] == self.oppCh() and \
                   D[row + 2][col - 2] == self.oppCh():
                    if col - 1 < 0 and row + 3 >= H:
                        return 2
                    return 1
                
        # diagonal leftUp to rightDown check
        for row in range(0, H - 2):
            for col in range(0, W - 2):
                if D[row][col] == self.oppCh() and \
                   D[row + 1][col + 1] == self.oppCh() and \
                   D[row + 2][col + 2] == self.oppCh():
                    if col + 3 >= W or row + 3 >= H:
                        return 2
                    return 1
        
        return -1
                
                
    def self3RunCase(self, b):
        D = b.data
        W = b.width
        H = b.height
        
        # self three run case
        # horizontal check
        for row in range(0, H):
            for col in range(0, W - 2):
                if D[row][col] == self.ox and \
                   D[row][col + 1] == self.ox and \
                   D[row][col + 2] == self.ox:
                    if col - 1 < 0 or col + 3 >= W:
                        return 2
                    return 1
                
        # vertical check       
        for row in range(0, H - 2):
            for col in range(0, W):
                if D[row][col] == self.ox and \
                   D[row + 1][col] == self.ox and \
                   D[row + 2][col] == self.ox:
                    if row - 1 < 0:
                        return 2
                    return 1
                 
        # diagonal leftDown to rightUp check
        for row in range(0, H - 2):
            for col in range(2, W):
                if D[row][col] == self.ox and \
                   D[row + 1][col - 1] == self.ox and \
                   D[row + 2][col - 2] == self.ox:
                    if col - 1 < 0 and row + 3 >= H:
                        return 2
                    return 1
                
        # diagonal leftUp to rightDown check     
        for row in range(0, H - 2):
            for col in range(0, W - 2):
                if D[row][col] == self.ox and \
                   D[row + 1][col + 1] == self.ox and \
                   D[row + 2][col + 2] == self.ox:
                    if col + 3 >= W or row + 3 >= H:
                        return 2
                    return 1
                
        return -1
                
    def self2RunCase(self, b):
        D = b.data
        W = b.width
        H = b.height
        
        # self two run case in beside empty        
        # horizontal check
        for row in range(0, H - 1):
            for col in range(1, W - 2):
                if D[row][col] == self.ox and \
                   D[row][col + 1] == self.ox:
                    if D[row + 1][col - 1] != ' ' and \
                       D[row + 1][col + 2] != ' ' and \
                       D[row][col - 1] == ' ' and \
                       D[row][col + 2] == ' ':
                        return True
        # 1st floor    
        row = b.height - 1          
        for col in range(1, W - 2):
            if D[row][col] == self.ox and \
               D[row][col + 1] == self.ox:
                if D[row][col - 1] == ' ' and \
                   D[row][col + 2] == ' ':
                    return True
                
        return False
        
class Player:
    
    def __init__(self, ox, tbt, ply):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s
    
    def oppCh(self):
        if self.ox is 'X':
            return 'O'
        else:
            return 'X'
        
    def scoreBoard(self, b):

        if b.winsFor(self.ox):
            return 100.0
        
        if b.winsFor(self.oppCh()):
            return 0.0
        
        return 50.0
    
    def tiebreakMove(self, scores):
        maxIndices = [i for i, x in enumerate(scores) if x == max(scores)]
        if self.tbt is "LEFT":
            return maxIndices[0]
        elif self.tbt is "RIGHT":
            return maxIndices[len(maxIndices) - 1]
        else:
            return random.choice(maxIndices)

    def scoresFor(self, b):
        W = b.width
        numericScores = [50.0] * W

        for index in range(W):
            if b.allowsMove(index) is False:
                numericScores[index] = -1.0
            elif self.ply is 0:
                numericScores[index] = self.scoreBoard(b)
            elif b.winsFor(self.ox) or b.winsFor(self.oppCh()) :
                numericScores[index] = self.scoreBoard(b)
            else :
                b.addMove(index, self.ox)
                opponent = Player(self.oppCh(), "RANDOM", self.ply - 1)
                oppScore = opponent.scoresFor(b)
                oppMax = max(oppScore)
                numericScores[index] = 100 - oppMax;
                b.delMove(index)
        return numericScores

    def nextMove(self, b):
        return self.tiebreakMove(self.scoresFor(b))
    


class Player2:
    
    def __init__(self, ox, tbt, ply):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s
    
    def oppCh(self):
        if self.ox is 'X':
            return 'O'
        else:
            return 'X'
    def scoreBoard(self, b):

        if b.winsFor(self.ox):
            return 100.0
        
        if b.winsFor(self.oppCh()):
            return 0.0
        
        return 50.0
        
    def scoreBoard4Tourney(self, b):

        maxTable = [[3,4,5,7,5,4,3],
                    [4,6,8,10,8,6,4],
                    [5,8,11,13,11,8,5],
                    [5,8,11,13,11,8,5],
                    [4,6,8,10,8,6,4],
                    [3,4,5,7,5,4,3]]

        weightList = [0,0,0,0,0,0,0]

        for col in range(b.width):
            for row in range(b.height-1, 0, -1):
                if b.data[row][col] == ' ':
                    weightList[col] = maxTable[row][col]
                    break


        if b.winsFor(self.ox):
            return 100.0
        
        if b.winsFor(self.oppCh()):
            return 0.0

        return 50.0
    
    def tiebreakMove(self, scores):
        maxIndices = [i for i, x in enumerate(scores) if x == max(scores)]
        if self.tbt is "LEFT":
            return maxIndices[0]
        elif self.tbt is "RIGHT":
            return maxIndices[len(maxIndices) - 1]
        else:
            return random.choice(maxIndices)

    def scoresFor(self, b):
        W = b.width
        numericScores = [50.0] * W
        for index in range(W):
            if b.allowsMove(index) is False:
                numericScores[index] = -1.0
            elif self.ply is 0:
                numericScores[index] = self.scoreBoard(b)
            elif b.winsFor(self.ox) or b.winsFor(self.oppCh()):
                numericScores[index] = self.scoreBoard(b)
            else:
                b.addMove(index, self.ox)
                opponent = Player2(self.oppCh(), "RANDOM", self.ply - 1)
                oppScore = opponent.scoresFor(b)
                oppMax = max(oppScore)
                if oppMax is -1:
                    oppMax = 10.0
                numericScores[index] = 100 - oppMax;
                b.delMove(index)

        if self.ply is 4:
            numericScores = self.getWeightList(b,numericScores)

        return numericScores

    def getWeightList(self, b, numericScores):
        maxTable = [[3,4,5,7,5,4,3],
                    [4,6,8,10,8,6,4],
                    [5,8,11,13,11,8,5],
                    [5,8,11,13,11,8,5],
                    [4,6,8,10,8,6,4],
                    [3,4,5,7,5,4,3]]

        weightList = [0,0,0,0,0,0,0]

        for col in range(b.width):
            for row in range(b.height-1, 0, -1):
                if b.data[row][col] == ' ':
                    weightList[col] = maxTable[row][col]
                    break

        defenceIndex = [defenceIndex for defenceIndex, x in enumerate(numericScores) if x == max(numericScores)]

        if len(defenceIndex) is 1:
            return numericScores

        if len(defenceIndex) is 2:
            numericScores[defenceIndex[0]] = 70.0
            numericScores[defenceIndex[1]] = 70.0

        if len(defenceIndex) is 3:
            numericScores[defenceIndex[0]] = 70.0
            numericScores[defenceIndex[1]] = 70.0
            numericScores[defenceIndex[2]] = 70.0
         
        (maxWeight,maxWeightIndex) = max((maxWeight,maxWeightIndex) for maxWeightIndex,maxWeight in enumerate (weightList))

        if numericScores[maxWeightIndex] is 0.0:
            numericScores[maxWeightIndex] = 0.0
        else:
            numericScores[maxWeightIndex] = 60.0

        return numericScores

    def nextMove(self, b):
        return self.tiebreakMove(self.scoresFor(b))
    
# b = Board(7, 6)numericScores[index]
# b.setBoard( '1211244445' )
# print(b)

# p = Player( 'X', 'LEFT', 0 )
# print(p.scoreBoard(b))

# print(Player('O', 'LEFT', 0).scoreBoard(b))

# print(Player('O', 'LEFT', 0).scoreBoard( Board(7,6) ))



# scores = [0, 0, 50, 0, 50, 50, 0]
# p = Player('X', 'LEFT', 1)
# p2 = Player('X', 'RIGHT', 1)
# p3 = Player('X', 'RANDOM', 1)

# print(p.tiebreakMove(scores))
# print(p2.tiebreakMove(scores))
# print(p3.tiebreakMove(scores))
# b=Board(7,6)
# b.setBoard('1211244445')
# # 
# print(Player('X', 'LEFT', 0).scoresFor(b))
# print(Player('O', 'LEFT', 1).scoresFor(b))
# print(Player('X', 'LEFT', 2).scoresFor(b))
# print(Player('X', 'LEFT', 3).scoresFor(b))
# print(Player('O', 'LEFT', 3).scoresFor(b))
# print(Player('O', 'LEFT', 4).scoresFor(b))

class scoreCounter:
    xWinCount=0
    oWinCount=0

    def xWin(self):
        self.xWinCount+=1

    def oWin(self):
        self.oWinCount+=1

player = Player('X','RANDOM',4)
human = Player2('O','RANDOM',4)

sc = scoreCounter()

for x in xrange(1,2):
    b = Board(7,6)
    b.playGame(player, human, sc)

print "Owin:" + str(sc.oWinCount) + "   "+ "Xwin:" + str(sc.xWinCount)


   # D = b.data
        # W = b.width
        # H = b.height
        
        # # opp three run case
        # # horizontal check
        # for row in range(0, H):
        #     for col in range(0, W - 2):
        #         if D[row][col] == self.oppCh() and \
        #            D[row][col + 1] == self.oppCh() and \
        #            D[row][col + 2] == self.oppCh():
        #             if col - 1 < 0 or col + 3 >= W:
        #                 return 50.0
        #             return 30.0
                
        # # vertical check       
        # for row in range(0, H - 2):
        #     for col in range(0, W):
        #         if D[row][col] == self.ox and \
        #            D[row + 1][col] == self.ox and \
        #            D[row + 2][col] == self.ox:
        #             if row - 1 < 0:
        #                 return 50.0
        #             return 30.0
                 
        # # diagonal leftDown to rightUp check
        # for row in range(0, H - 2):
        #     for col in range(2, W):
        #         if D[row][col] == self.oppCh() and \
        #            D[row + 1][col - 1] == self.oppCh() and \
        #            D[row + 2][col - 2] == self.oppCh():
        #             if col - 1 < 0 and row + 3 >= H:
        #                 return 50.0
        #             return 30.0
                
        # # diagonal leftUp to rightDown check
        # for row in range(0, H - 2):
        #     for col in range(0, W - 2):
        #         if D[row][col] == self.oppCh() and \
        #            D[row + 1][col + 1] == self.oppCh() and \
        #            D[row + 2][col + 2] == self.oppCh():
        #             if col + 3 >= W or row + 3 >= H:
        #                 return 50.0
        #             return 30.0
        
        
        # # self three run case
        # # horizontal check
        # for row in range(0, H):
        #     for col in range(0, W - 2):
        #         if D[row][col] == self.ox and \
        #            D[row][col + 1] == self.ox and \
        #            D[row][col + 2] == self.ox:
        #             if col - 1 < 0 or col + 3 >= W:
        #                 return 60.0
        #             return 80.0
                
        # # vertical check       
        # for row in range(0, H - 2):
        #     for col in range(0, W):
        #         if D[row][col] == self.ox and \
        #            D[row + 1][col] == self.ox and \
        #            D[row + 2][col] == self.ox:
        #             if row - 1 < 0:
        #                 return 60.0
        #             return 80.0
                 
        # # diagonal leftDown to rightUp check
        # for row in range(0, H - 2):
        #     for col in range(2, W):
        #         if D[row][col] == self.ox and \
        #            D[row + 1][col - 1] == self.ox and \
        #            D[row + 2][col - 2] == self.ox:
        #             if col - 1 < 0 and row + 3 >= H:
        #                 return 60.0
        #             return 80.0
                
        # # diagonal leftUp to rightDown check     
        # for row in range(0, H - 2):
        #     for col in range(0, W - 2):
        #         if D[row][col] == self.ox and \
        #            D[row + 1][col + 1] == self.ox and \
        #            D[row + 2][col + 2] == self.ox:
        #             if col + 3 >= W or row + 3 >= H:
        #                 return 60.0
        #             return 80.0
        
        
        # # self two run case in beside empty        
        # # horizontal check
        # for row in range(0, H - 1):
        #     for col in range(1, W - 1):
        #         if D[row][col] == self.ox and \
        #            D[row][col + 1] == self.ox:
        #             if D[row + 1][col - 1] != ' ' and \
        #                D[row + 1][col + 1] != ' ' and \
        #                D[row][col - 1] == ' ' and \
        #                D[row][col + 1] == ' ':
        #                 return 70.0
        # # 1st floor    
        # row = b.height - 1          
        # for col in range(1, H - 1):
        #     if D[row][col] == self.ox and \
        #        D[row][col + 1] == self.ox:
        #         if D[row][col - 1] == ' ' and \
        #            D[row][col + 1] == ' ':
        #             return 70.0
