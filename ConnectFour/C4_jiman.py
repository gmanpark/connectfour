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
    


class Player_PP:
    
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

    def getWeightList(self, numericScores, b):
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

        (maxWeight,maxWeightIndex) = max((maxWeight,maxWeightIndex) for maxWeightIndex,maxWeight in enumerate (weightList))

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

        if len(defenceIndex) is 4:
            numericScores[defenceIndex[0]] = 70.0
            numericScores[defenceIndex[1]] = 70.0
            numericScores[defenceIndex[2]] = 70.0

        # if len(defenceIndex) is 7:
        #     if b.data[3][3] is " ":
        #         if b.data[5][3] is self.oppCh():
        #             if b.data[4][3] is self.ox:
        #                 if b.data[5][4] is self.oppCh():
        #                     numericScores[2] = 60.0
        #                 elif b.data[5][2] is self.oppCh():
        #                     numericScores[4] = 60.0
                    
        if numericScores[maxWeightIndex] is 0.0:
            numericScores[maxWeightIndex] = 0.0
        elif numericScores[maxWeightIndex] != -1.0:
            if numericScores[maxWeightIndex] < 55.0:
                numericScores[maxWeightIndex] = 55.0


        return numericScores

    def scoreBoard4Tourney(self, b):
        if b.winsFor(self.ox):
            return 100.0
        
        elif b.winsFor(self.oppCh()):
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
            else:
                b.addMove(index, self.ox)
                opponent = Player_PP(self.oppCh(), "RANDOM", self.ply - 1)
                oppScore = opponent.scoresFor(b)
                oppMax = max(oppScore)

                if oppMax is -1.0:
                    oppMax = 10.0
                numericScores[index] = 100 - oppMax
                b.delMove(index)

        return numericScores

    def nextMove(self, b):
        return self.tiebreakMove(self.getWeightList(self.scoresFor(b),b))

#-*- coding: utf-8 -*-
'''
Created on 2014. 2. 3.

@author: Gwon Gi-soo, Yoon Sung-tak
'''
# -*- coding: cp949 -*-
import random
from random import shuffle
class Player4Tourney:

    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        if self.ox == 'X' :
            return 'O'
        return 'X'

    def sumOppCheckerWeight(self, board):
        self.ox = self.oppCh()
        oppCheckerWeight = self.sumCheckerWeight(board)
        self.ox = self.oppCh()
        return oppCheckerWeight

    def scoreBoard4Tourney(self, board):
        if board.winsFor(self.ox):
            return 100.0
        elif board.winsFor(self.oppCh()):
            return 0.0
        return 50.0 + self.sumCheckerWeight(board) - self.sumOppCheckerWeight(board)
    
    def checkFreeTwoChecker(self, board):
        freeRow = board.height - 1
        data = board.data
        for col in range(1, board.width - 2):
            if data[freeRow][col-1] == ' ' and data[freeRow][col] == self.ox and data[freeRow][col+1] == self.ox and data[freeRow][col+2] == ' ':
                return True
        for col in range(1, board.width - 3):
            if data[freeRow][col-1] == ' ' and data[freeRow][col] == self.ox and data[freeRow][col+1] == ' ' and data[freeRow][col+2] == self.ox and data[freeRow][col+3] == ' ':
                return True
        return False
    
    def sumCheckerWeight(self, board):
        return (self.horizontalWeight(board) + self.verticalWeight(board) + self.rightDownWeight(board) + self.leftDownWeight(board)) / 1000.0
    
    def horizontalWeight(self, board):
        sumWeight = 0
        colLimit = board.width - 3
        data = board.data
        for row in range(board.height):
            for col in range(colLimit):                 
                myCnt, oppCnt, blankCnt = self.countChecker([data[row][col], data[row][col+1], data[row][col+2], data[row][col+3]])
                
                if(oppCnt > 0):
                    continue
                sumWeight += myCnt * myCnt * myCnt * myCnt
        return sumWeight
                
    
    def verticalWeight(self, board):
        sumWeight = 0
        rowLimit = board.height - 3
        data = board.data
        for row in range(rowLimit):
            for col in range(board.width):
                myCnt, oppCnt, blankCnt = self.countChecker([data[row][col], data[row+1][col], data[row+2][col], data[row+3][col]])
                
                if(oppCnt > 0):
                    continue
                sumWeight += myCnt * myCnt * myCnt * myCnt
        return sumWeight
    
    def rightDownWeight(self, board):
        sumWeight = 0
        rowLimit = board.height - 3
        colLimit = board.width - 3
        data = board.data
        for row in range(rowLimit):
            for col in range(colLimit):
                myCnt, oppCnt, blankCnt = self.countChecker([data[row][col], data[row+1][col+1], data[row+2][col+2], data[row+3][col+3]])
                
                if(oppCnt > 0):
                    continue
                sumWeight += myCnt * myCnt * myCnt * myCnt
        return sumWeight
    
    def leftDownWeight(self, board):
        sumWeight = 0
        rowLimit = board.height - 3
        colStart = 3
        data = board.data
        for row in range(rowLimit):
            for col in range(colStart, board.width):
                myCnt, oppCnt, blankCnt = self.countChecker([data[row][col], data[row+1][col-1], data[row+2][col-2], data[row+3][col-3]])
                
                if(oppCnt > 0):
                    continue
                sumWeight += myCnt * myCnt * myCnt * myCnt
        return sumWeight
            
    def countChecker(self, checkers):
        myChecker = self.ox
        oppChecker = self.oppCh()
        myCount = oppCount = blankCount = 0
        for checker in checkers:
            if checker == myChecker:
                myCount += 1
            elif checker == oppChecker:
                oppCount += 1
            else:
                blankCount += 1
        return myCount, oppCount, blankCount

    def tiebreakMove(self, scores):
        scoreMax = max(scores)
        
        maxIndices = []
        for i in range(len(scores)):
            score = scores[i]
            if score == scoreMax:
                maxIndices.append(i)
                
        if self.tbt == 'LEFT':
            return maxIndices[0]
        elif self.tbt == 'RIGHT':
            return maxIndices[len(maxIndices) - 1]
        else:
            randomList = range(len(maxIndices))
            shuffle(randomList)
            return maxIndices[randomList[0]]

    def scoresFor(self, board):
        if board.winsFor(self.oppCh()):
            return [0] * board.width
        if self.checkFreeTwoChecker(board):
            return [100] * board.width
        
        scores = [50.0] * board.width 

        for col in range(board.width):
            if board.allowsMove(col) == False:
                scores[col] = -1.0            
                continue
            
            if self.ply == 0:
                board.addMove(col, self.ox)
                scores[col] = self.scoreBoard4Tourney(board)
                board.delMove(col)
                continue

            board.addMove(col, self.ox)
            oppPlayer = Player4Tourney(self.oppCh(), 'RANDOM', self.ply - 1)                
            oppScores = oppPlayer.scoresFor(board)                     
            maxOppScore = max(oppScores)
            #All full score max value is -1.0 become exception 
            if maxOppScore >= 0 :
                scores[col] = 100 - maxOppScore
            else:
                scores[col] = self.scoreBoard4Tourney(board)
            board.delMove(col)
        return scores

    def nextMove(self, board):
        scores = self.scoresFor(board)
        return self.tiebreakMove(scores)

class MoonsPlayer:
    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt
        self.ply = ply
        
    def __repr__(self):
        s = "Player for " + self.ox + "\n"
        s += " with tiebreak type: " + self.tbt + "\n"
        s += " and ply == " + str(self.ply) + "\n\n"
        return s
    
    def oppCh(self):
        if self.ox == 'X':
            return 'O'
        return 'X'
    
    def scoreBoard(self, b):
        if b.winsFor(self.ox):
            return 100.0
        elif b.winsFor(self.oppCh()):
            return 0.0
        return 50.0
    
    def tiebreakMove(self, scores):
        
        maxScore = max(scores)
        readRange = [0]
        tiebreak = self.tbt
        if tiebreak == "RANDOM":
            random_tiebreak = random.randint(0, 1)
            if random_tiebreak == 0:
                tiebreak = 'LEFT'
            else:
                tiebreak = 'RIGHT'
            
        if tiebreak == "LEFT":
            readRange = range(0, len(scores))
        else:
            readRange = range(len(scores) - 1, -1, -1)
        for indice in readRange:
            if maxScore == scores[indice]:
                return indice
        
            
    def scoresFor(self, b):
        score = [50] * b.width
        
        for i in range(0, b.width):
            if b.allowsMove(i) == False:
                score[i] = -1.0
                continue
            
            if b.winsFor(self.ox) or b.winsFor(self.oppCh()):
                score[i] = self.scoreBoard(b)
                continue
                
            if self.ply == 0:
                score[i] = self.scoreBoard(b)
                continue
                
            b.addMove(i, self.ox)
            
            oppScoreBoard = Player(self.oppCh(), 'RANDOM', self.ply - 1).scoresFor(b)
            oppScore = max(oppScoreBoard)
            score[i] = 100.0 - oppScore
                
            b.delMove(i)
        
        return score
    
    def nextMove(self, b):
        return self.tiebreakMove(self.scoreBoard4Tourney(b))
    
#   when circle is in a row (direction : horizontal) count the number of circle and return the count    
    def horizontalScore(self, i, b):
        col = i
        row = self.colStack(b, i)
        count = 0
        # left check
        while row < b.height and col < b.width:
            if b.data[row][col] == self.ox:
                col += 1
                count += 1
            else:
                break
            
        # right check
        col = i
        while row < b.height and col >= 0:
            col -= 1
            if b.data[row][col] == self.ox:
                count += 1
            else:
                break
        return count
#   when circle is in a row (direction : verical) count the number of circle and return the count
    def verticalScore(self, i, b):
        count = 0
        for row in range(b.height - self.colStack(b, i) + 1, b.height):
            if b.data[row][i] == self.ox:
                count += 1
            else:
                break
        if (b.height - self.colStack(b, i) == 0) and count <= 3:
            return 0
        return count
    
#   when circle is in a row (direction : leftDiagnal) count the number of circle and return the count
    def leftDiagonalScore(self, i, b):
        count = 0
        D = b.data
        col = i
        row = b.height - self.colStack(b, i)
        while row < b.height and col < b.width:
            if D[row][col] == self.ox:
                count += 1
                row += 1
                col += 1
            else:
                break
        
        col = i
        row = b.height - self.colStack(b, i)
        while row >= 0 or col >=0 :
            if D[row][col] == self.ox:
                count += 1
                row -= 1
                col -= 1
            else:
                break
        return count
    
#   when circle is in a row, (direction : rightDiagnal) count the number of circle and return the count
    def rightDiagonalScore(self, i, b):
            count = 0
            D = b.data
            col = i
            row = b.height - self.colStack(b, i)
            while row > 0 and col < b.width:
                if D[row][col] == self.ox:
                    count += 1
                    row -= 1
                    col += 1
                else:
                    break
            
            col = i
            row = b.height - self.colStack(b, i)
            while row < b.height and col >= 0:
                if D[row][col] == self.ox:
                    count += 1
                    row += 1
                    col -= 1
                else:
                    break
            return count
        
    def scoreBoard4Tourney(self, b):
        score = [100] * b.width
        score[3] += 2

        for i in range(0, b.width):
            if b.allowsMove(i) == False:
                score[i] = -1.0
                continue
            
            if b.winsFor(self.ox) or b.winsFor(self.oppCh()):
                score[i] = self.scoreBoard(b)
                continue
                
            if self.ply == 0:
                score[i] = self.scoreBoard(b)
                continue
                
            b.addMove(i, self.ox)
            
            score[i] += self.horizontalScore(i, b)
            score[i] += self.verticalScore(i, b)
            score[i] += self.leftDiagonalScore(i, b)
            score[i] += self.rightDiagonalScore(i, b)

            oppScoreBoard = MoonsPlayer(self.oppCh(), 'RANDOM', self.ply - 1).scoreBoard4Tourney(b)
            oppScore = max(oppScoreBoard)
            score[i] = score[i] - oppScore
            
            b.delMove(i)
        # 예외 처리
        if max(score) < 0.0:
            for i in range(0, 7):
                score[i] *= -1.0
                if b.allowsMove(i) == True:
                    score[i] = 10.0
        return score
    
    def colStack(self, b, col):
        H = b.height
        D = b.data
        count = 0
        for row in range(H - 1, -1, -1):
            if D[row][col] == ' ':
                return count
            count += 1
        return count

class scoreCounter:
    xWinCount = 0
    oWinCount = 0

    def xWin(self):
        self.xWinCount+=1

    def oWin(self):
        self.oWinCount+=1

class Player_YUN:
    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt
        self.ply = ply
        self.columnScore = [3,4,5,5,5,4,3]

    def __repr__(self):
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        if self.ox is 'X':
            return 'O'
        else:
            return 'X'
    
    def checkBlank(self,board, row, col):
        for index in range(board.height-1,row,-1):
            if board.data[index][col] is ' ' :
                return False
        return True

    def checkFor3Blank(self, board, ox):
        if self.checkFor3BlankInDiagonalLine(board,ox) :
            return True
        if self.checkFor3BlankInHorisontalLine(board,ox) :
            return True     
        return False
    
    def checkFor3BlankInDiagonalLine(self,board, ox):
        for row in range(0, board.height - 4):
            for col in range(0, board.width - 4):
                if board.data[row][col] is ' ' and board.data[row + 1][col + 1] is ox and board.data[row + 2][col + 2] is ' ' and board.data[row + 3][col + 3] is ox and board.data[row + 4][col + 4] is ' ' :
                    if self.checkBlank(board,row, col) and self.checkBlank(board,row+2, col+2) and self.checkBlank(board,row+4, col+4) : 
                        return True

        for row in range(board.height - 1, 3, -1):
            for col in range(0, board.width - 4):
                if board.data[row][col] is ' ' and board.data[row - 1][col + 1] is ox and board.data[row - 2][col + 2] is ' ' and board.data[row - 3][col + 3] is ox and board.data[row - 4][col + 4] is ' ':
                    if self.checkBlank(board,row, col) and self.checkBlank(board,row-2, col+2)  and self.checkBlank(board,row-4, col+4) : 
                        return True
        return False
    
    def checkFor3BlankInHorisontalLine(self,board, ox):
        for row in range(0,board.height):
            for col in range(0,board.width-4):
                if board.data[row][col] is ' ' and board.data[row][col+1] is ox and board.data[row][col+2] is ' ' and board.data[row][col+3] is ox and board.data[row][col+4] is ' ':
                    if self.checkBlank(board,row, col) and self.checkBlank(board,row, col+2) and self.checkBlank(board,row, col+4) : 
                        return True
        return False
                
    def checkFor2Blank(self,board, ox):
        if self.checkFor2BlankInDiagonalLine(board,ox) :
            return True
        if self.checkFor2BlankInHorisontalLine(board,ox) :
            return True
        if self.checkFor2BlankInVerticalLine(board,ox) :
            return True       
        return False
    
    def checkFor2BlankInDiagonalLine(self,board, ox):
        for row in range(0, board.height - 3):
            for col in range(0, board.width - 3):
                if board.data[row][col] is ' ' and board.data[row + 1][col + 1] is ox and board.data[row + 2][col + 2] is ox and board.data[row + 3][col + 3] is ' ':
                    if self.checkBlank(board,row, col) and self.checkBlank(board,row+3, col+3) : 
                        return True 
                
               
        for row in range(board.height - 1, 2, -1):
            for col in range(0, board.width - 3):
                if board.data[row][col] is ' ' and board.data[row - 1][col + 1] is ox and board.data[row - 2][col + 2] is ox and board.data[row - 3][col + 3] is ' ':
                    if self.checkBlank(board,row, col) and self.checkBlank(board,row-3, col+3) : 
                        return True
        return False
    
    def checkFor2BlankInHorisontalLine(self,board, ox):
        for row in range(0,board.height):
            for col in range(0,board.width-3):
                if board.data[row][col] is ' ' and board.data[row][col+1] is ox and board.data[row][col+2] is ox and board.data[row][col+3] is ' ':
                    if self.checkBlank(board,row, col) and self.checkBlank(board,row, col+3) : 
                        return True
        return False
                
    def checkFor2BlankInVerticalLine(self,board, ox):
        for row in range(0,board.height-3):
            for col in range(0,board.width):
                if board.data[row][col] is ' ' and board.data[row+1][col] is ' ' and board.data[row+2][col] is ox and board.data[row+3][col] is ox:
                    return True
        return False
    
    def checkFor1Blank(self, board, ox):
        if self.checkFor1BlankInDiagonalLine(board,ox) :
            return True
        if self.checkFor1BlankInHorisonalLine(board,ox) :
            return True
        if self.checkFor1BlankInVerticalLine(board,ox) :
            return True       
        return False
    
    def checkFor1BlankInDiagonalLine(self,board, ox):
        for row in range(0, board.height - 3):
            for col in range(0, board.width - 3):
                if board.data[row][col] is ' ' and board.data[row + 1][col + 1] is ox and board.data[row + 2][col + 2] is ox and board.data[row + 3][col + 3] is ox:
                    if self.checkBlank(board,row, col) :
                        return True
                if board.data[row][col] is ox and board.data[row + 1][col + 1] is ' ' and board.data[row + 2][col + 2] is ox and board.data[row + 3][col + 3] is ox:
                    if self.checkBlank(board,row+1, col+1) :
                        return True
                if board.data[row][col] is ox and board.data[row + 1][col + 1] is ox and board.data[row + 2][col + 2] is ' ' and board.data[row + 3][col + 3] is ox:
                    if self.checkBlank(board,row+2, col+2) :
                        return True
                if board.data[row][col] is ox and board.data[row + 1][col + 1] is ox and board.data[row + 2][col + 2] is ox and board.data[row + 3][col + 3] is ' ':
                    if self.checkBlank(board,row+3, col+3) :
                        return True
        for row in range(board.height - 1, 2, -1):
            for col in range(0, board.width - 3):
                if board.data[row][col] is ' ' and board.data[row - 1][col + 1] is ox and board.data[row - 2][col + 2] is ox and board.data[row - 3][col + 3] is ox:
                    if self.checkBlank(board,row, col) :
                        return True
                if board.data[row][col] is ox and board.data[row - 1][col + 1] is ' ' and board.data[row - 2][col + 2] is ox and board.data[row - 3][col + 3] is ox:
                    if self.checkBlank(board,row-1, col+1) :
                        return True
                if board.data[row][col] is ox and board.data[row - 1][col + 1] is ox and board.data[row - 2][col + 2] is ' ' and board.data[row - 3][col + 3] is ox:
                    if self.checkBlank(board,row-2, col+2) :
                        return True
                if board.data[row][col] is ox and board.data[row - 1][col + 1] is ox and board.data[row - 2][col + 2] is ox and board.data[row - 3][col + 3] is ' ':
                    if self.checkBlank(board,row-3, col+3) :
                        return True
        return False
    
    def checkFor1BlankInHorisonalLine(self,board, ox):
        for row in range(0,board.height):
            for col in range(0,board.width-3):
                if board.data[row][col] is ' ' and board.data[row][col+1] is ox and board.data[row][col+2] is ox and board.data[row][col+3] is ox:
                    if self.checkBlank(board,row, col) :
                        return True
                if board.data[row][col] is ox and board.data[row][col+1] is ' ' and board.data[row][col+2] is ox and board.data[row][col+3] is ox:
                    if self.checkBlank(board,row, col+1) :
                        return True
                if board.data[row][col] is ox and board.data[row][col+1] is ox and board.data[row][col+2] is ' ' and board.data[row][col+3] is ox:
                    if self.checkBlank(board,row, col+2) :
                        return True
                if board.data[row][col] is ox and board.data[row][col+1] is ox and board.data[row][col+2] is ox and board.data[row][col+3] is ' ':
                    if self.checkBlank(board,row, col+3) :
                        return True
        return False
                
    def checkFor1BlankInVerticalLine(self,board, ox):
        for row in range(0,board.height-3):
            for col in range(0,board.width):
                if board.data[row][col] is ' ' and board.data[row+1][col] is ox and board.data[row+2][col] is ox and board.data[row+3][col] is ox:
                    return True
        return False
                
    def checkBlankCount(self,board, row, col):
        count = 0
        for index in range(board.height-1,row+1,-1):
            if board.data[index][col] is ' ' :
                count += 1
        return count % 2
    
    def checkFor1BlankWithBlankCount(self, board, ox):
        if self.checkFor1BlankInDiagonalLineWithBlankCount(board,ox) :
            return True
        if self.checkFor1BlankInHorisontalLineWithBlankCount(board,ox) :
            return True
        return False
    
    def checkFor1BlankInDiagonalLineWithBlankCount(self,board, ox):
        for row in range(0, board.height - 3):
            for col in range(0, board.width - 3):
                if board.data[row][col] is ' ' and board.data[row + 1][col + 1] is ox and board.data[row + 2][col + 2] is ox and board.data[row + 3][col + 3] is ox:
                    if self.checkBlankCount(board,row, col) == 1 :
                        return True
                if board.data[row][col] is ox and board.data[row + 1][col + 1] is ' ' and board.data[row + 2][col + 2] is ox and board.data[row + 3][col + 3] is ox:
                    if self.checkBlankCount(board,row+1, col+1) == 1 :
                        return True
                if board.data[row][col] is ox and board.data[row + 1][col + 1] is ox and board.data[row + 2][col + 2] is ' ' and board.data[row + 3][col + 3] is ox:
                    if self.checkBlankCount(board,row+2, col+2) == 1 :
                        return True
                if board.data[row][col] is ox and board.data[row + 1][col + 1] is ox and board.data[row + 2][col + 2] is ox and board.data[row + 3][col + 3] is ' ':
                    if self.checkBlankCount(board,row+3, col+3) == 1 :
                        return True
        for row in range(board.height - 1, 2, -1):
            for col in range(0, board.width - 3):
                if board.data[row][col] is ' ' and board.data[row - 1][col + 1] is ox and board.data[row - 2][col + 2] is ox and board.data[row - 3][col + 3] is ox:
                    if self.checkBlankCount(board,row, col) == 1 :
                        return True
                if board.data[row][col] is ox and board.data[row - 1][col + 1] is ' ' and board.data[row - 2][col + 2] is ox and board.data[row - 3][col + 3] is ox:
                    if self.checkBlankCount(board,row-1, col+1) == 1 :
                        return True
                if board.data[row][col] is ox and board.data[row - 1][col + 1] is ox and board.data[row - 2][col + 2] is ' ' and board.data[row - 3][col + 3] is ox:
                    if self.checkBlankCount(board,row-2, col+2) == 1 :
                        return True
                if board.data[row][col] is ox and board.data[row - 1][col + 1] is ox and board.data[row - 2][col + 2] is ox and board.data[row - 3][col + 3] is ' ':
                    if self.checkBlankCount(board,row-3, col+3) == 1 :
                        return True
        return False
    
    def checkFor1BlankInHorisontalLineWithBlankCount(self,board, ox):
        for row in range(0,board.height):
            for col in range(0,board.width-3):
                if board.data[row][col] is ' ' and board.data[row][col+1] is ox and board.data[row][col+2] is ox and board.data[row][col+3] is ox:
                    if self.checkBlankCount(board,row, col) == 1 :
                        return True
                if board.data[row][col] is ox and board.data[row][col+1] is ' ' and board.data[row][col+2] is ox and board.data[row][col+3] is ox:
                    if self.checkBlankCount(board,row, col+1) == 1 :
                        return True
                if board.data[row][col] is ox and board.data[row][col+1] is ox and board.data[row][col+2] is ' ' and board.data[row][col+3] is ox:
                    if self.checkBlankCount(board,row, col+2) == 1 :
                        return True
                if board.data[row][col] is ox and board.data[row][col+1] is ox and board.data[row][col+2] is ox and board.data[row][col+3] is ' ':
                    if self.checkBlankCount(board,row, col+3) == 1 :
                        return True
        return False
     
    def scoreBoard4Tourney(self, board):
        if board.winsFor(self.ox): 
            return 100.0
        
        if board.winsFor(self.oppCh()): 
            return 0.0
        
        if self.checkFor1Blank(board,self.ox):
            return 90.0
        
        if self.checkFor1Blank(board,self.oppCh()):
            return 10.0
           
        if self.checkFor3Blank(board,self.ox):
            return 80.0
        
        if self.checkFor3Blank(board,self.oppCh()):
            return 20.0
        
        if self.checkFor1BlankWithBlankCount(board,self.ox):
            return 70.0
        
        if self.checkFor1BlankWithBlankCount(board,self.oppCh()):
            return 30.0
        
        if self.checkFor2Blank(board,self.ox):
            return 60.0

        if self.checkFor2Blank(board,self.oppCh()):
            return 40.0
        
        return 50.0
       
    def scoreBoard(self, board):
        if board.winsFor(self.ox): 
            return 100.0
        
        if board.winsFor(self.oppCh()):
            return 0.0

        return 50.0
    
    def tiebreakMove(self, scores):
        for index in range(len(scores)):
            if scores[index] == -1.0 :
                continue
            scores[index] += self.columnScore[index]
        maxIndices = [i for i,x in enumerate(scores) if x == max(scores)]
        
        if self.tbt is 'LEFT':
            return maxIndices[0]
        
        elif self.tbt is 'RIGHT':
            return maxIndices[len(maxIndices)-1]     
        
        elif self.tbt is 'RANDOM':
            return random.choice(maxIndices)

    def scoresFor(self,board):
        scoreArray = [50.0]*board.width

        for col in range(board.width):
            if board.winsFor(self.ox) is True :
                break
            
            if board.allowsMove(col) == False:
                scoreArray[col] = -1.0
                continue
            
            if self.ply == 0 :
                scoreArray[col] = self.scoreBoard4Tourney(board)
                continue
            
            board.addMove(col,self.ox)
            if board.winsFor(self.ox) is True :
                scoreArray[col] = 100.0
                board.delMove(col)
                continue
            
            oppPlayer = Player(self.oppCh(), self.tbt, self.ply-1)
            oppScore = oppPlayer.scoresFor(board)
            oppMax = max(oppScore)
            scoreArray[col] = 100 - oppMax
            board.delMove(col)
        return scoreArray
    
    def nextMove(self, board):
        scoreArray = self.scoresFor(board)
        return self.tiebreakMove(scoreArray) 

class PortalPlayer:

    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt
        self.ply = ply
        
    def __repr__(self):
        s = "PortalPlayer for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        print s
        
    def oppCh(self):
        if self.ox == 'X':
            return 'O'
        else: return 'X'
    
    def scoreBoard(self, b):
        if b.winsFor(self.oppCh()) == True:
            return 0.0
        elif b.winsFor(self.ox) == True:
            return 100.0
        else: return 50.0
        
    def tiebreakMove(self, scores):
        maxIndices = []
        maxValue = max(scores)
        index = 0
        while index < len(scores):
            if scores[index] == maxValue:
                maxIndices.append(index)
            index += 1
        
        if len(maxIndices) == 1:
            return maxIndices[0]
        else:
            if self.tbt == 'LEFT':
                return maxIndices[0]
            elif self.tbt == 'RIGHT':
                return maxIndices[len(maxIndices) - 1]
            else: 
                return maxIndices[random.randint(0, len(maxIndices) - 1)]
                
        
    def scoresFor(self, b):
        scores = [0.0] * b.width
        for col in range(b.width):
            """ ply = 0일 때"""
            if self.ply == 0: 
                for index in range(b.width):
                    if b.allowsMove(index) == True:
                        scores[index] = self.scoreBoard4Tourney(b)
                    else: scores[index] = -2000.0
                return scores
            """ ply가 0 이상일 때 """
            if b.allowsMove(col) == False:  # 해당 column이 이미 꽉찬경우 -1을 scores에 넣고 다음 column로 이동
                scores[col] = -2000.0
                continue
            b.addMove(col, self.ox) 
            if b.isFull() == True:
                scores[col] = 0.0
                b.delMove(col)
                continue
            if b.winsFor(self.ox) == True:
                scores[col] = 2000.0
                b.delMove(col)
                continue
            oppTurn = PortalPlayer(self.oppCh(), self.tbt, self.ply - 1)
            oppScores = oppTurn.scoresFor(b)
            oppMax = max(oppScores)
            scores[col] = -1 * oppMax
            b.delMove(col)
        
#         if scores[3] is max(scores):
#             if b.allowsMove(3) is True:
#                 scores[3] += 100
        return scores
  
    
    def scoreBoard4Tourney(self, b):
        """ < Game Heuristic > 
            1. board 내에서 위치 별로 가중치를 다르게 주어, 중앙에 놓인 돌 일수록 높은 점수를 갖는다. 
            2. 가로, 세로, ↘대각선, ↗ 대각선의 네 방향으로 인접한 돌의 갯수에 따른 가중치를 부여한다. 
            3. 1개의 돌 점수 : 네 방향 인접 가중치의 합 * 해당 돌의 위치 점수
            4. 전체 board의 점수 : 해당 User의 모든 돌의 점수의 합 
            5. 현재 board의 내 점수와 상대방 점수를 둘 다 계산하고, 
                - 내 점수가 높다면, 내가 유리한 것으로 가정, 공격형 전략을 택한다. (board 점수 = 내 점수)
                - 상대방 점수가 높다면, 상대방이 유리한 것으로 가정, 방어적 전략을 택한다. 현재 상태의 board가 피할수 있도록 점수를 최대한 낮게 준다.
                  (board 점수 = -1 * 상대방 점수)  
        """
        total = 0.0
        """ 전체 보드판에 놓여있는 나의 모든 돌을 돌며 점수를 계산한다"""
        for col in range(b.width):
            for row in range(b.height - 1, 0, -1):
                if self.doNotNeedCheck(b, row, col) == True: 
                    break
                place = self.getPlaceWeightAt(row, col)  # 해당하는 돌의 위치 가중치를 가져온다.(돌의 위치가 중앙일수록 점수가 높다.)
                rowScore = self.checkRow(row, col, b) 
                colScore = self.checkCol(row, col, b)
                firstDiagonalScore = self.checkFirstDiagonal(row, col, b)
                secondDiagonalScore = self.checkSecondDiagonal(row, col, b)

                adjacentScore = rowScore + colScore + firstDiagonalScore + secondDiagonalScore
                if adjacentScore == 0:
                    total += place
                else :
                    total += place * adjacentScore
        
        """ 현재 board의 상대방 점수를 위와 같은 방식으로 계산한다 """
        oppTotal = 0.0
        self.ox = self.oppCh()
        for col in range(b.width):
            for row in range(b.height - 1, 0, -1):
                if self.doNotNeedCheck(b, row, col) == True:
                    break
                place = self.getPlaceWeightAt(row, col)
                rowScore = self.checkRow(row, col, b)
                colScore = self.checkCol(row, col, b)
                firstDiagonalScore = self.checkFirstDiagonal(row, col, b)
                secondDiagonalScore = self.checkSecondDiagonal(row, col, b)

                temp = rowScore + colScore + firstDiagonalScore + secondDiagonalScore
                if temp == 0:
                    oppTotal += place
                else :
                    oppTotal += place * temp
        self.ox = self.oppCh()
        
        """ 나의 점수와 상대방 점수를 비교하여 공격/수비 전략을 택한다. """
        if total > oppTotal: return total
        else: return -1 * oppTotal
        
    def nextMove(self, b):
        col = self.tiebreakMove(self.scoresFor(b))
        print col
        return col
    
    """ 위치 별 가중치를 계산한다 """
    def getPlaceWeightAt(self, row, col):
        colScore = [1.0, 3.0, 6.0, 10.0, 6.0, 3.0, 1.0]  # 1, 3, 5, 7 -> 1, 3, 6, 10
        rowScore = [1.0, 3.0, 6.0, 6.0, 3.0, 1.0]
        return colScore[col] + rowScore[row]
    
    """ 세로로 인접한 돌의 갯수를 count하고, 갯수만큼의 가중치를 return """
    def checkCol(self, row, col, b):
        scoreList = [0.0, 3.0, 6.0, 10.0]
        
        count = 1
        emptySpace = 1
        for i in range(1, 6):
            if row + i < b.height:
                if b.data[row + i][col] is self.oppCh():
                    break
                elif b.data[row + i][col] is ' ':
                    if emptySpace is 0:
                        break
                    emptySpace -= 1
                    count += 1
                else: count += 1
        emptySpace = 1
        for i in range(1, 6):
            if row - i >= 0:
                if b.data[row - i][col] is self.oppCh():
                    break
                elif b.data[row - i][col] is ' ':
                    if emptySpace is 0:
                        break
                    emptySpace -= 1
                    count += 1
                else: count += 1
        return count * 2
    
    """ 가로로 인접한 돌의 갯수를 count하고, 갯수만큼의 가중치를 return """
    def checkRow(self, row, col, b):
        # scoreList = [0.0, 3.0, 6.0, 10.0]
        count = 1
        emptySpace = 1
        for i in range(1, 6):
            if col + i < b.width:
                if b.data[row][col + i] is self.oppCh():
                    break
                elif b.data[row][col + i] is ' ':
                    if emptySpace is 0:
                        break
                    emptySpace -= 1
                    count += 1
                else: count += 1
        emptySpace = 1
        for i in range(1, 6):
            if col - i >= 0:
                if b.data[row][col - i] is self.oppCh():
                    break
                elif b.data[row][col - i] is ' ':
                    if emptySpace is 0:
                        break
                    emptySpace -= 1
                    count += 1
                else: count += 1
        return count * 2 
    
    """ ↘ 방향 대각선으로 인접한 돌의 갯수를 count하고, 갯수만큼의 가중치를 return """
    def checkFirstDiagonal(self, row, col, b):
        scoreList = [0.0, 3.0, 6.0, 10.0]
        
        count = 1
        emptySpace = 1
        for i in range(1, 6):
            if col + i < b.width:
                if row + i < b.height:
                    if b.data[row + i][col + i] is self.oppCh():
                        break
                    elif b.data[row + i][col + i] is ' ':
                        if emptySpace is 0:
                            break
                        emptySpace -= 1
                        count += 1
                    else: count += 1
        
        emptySpace = 1
        for i in range(1, 6):
            if col - i >= 0:
                if row - i >= 0:
                    if b.data[row - i][col - i] is self.oppCh():
                        break
                    elif b.data[row - i][col - i] is ' ':
                        if emptySpace is 0:
                            break
                        emptySpace -= 1
                        count += 1
                    else: count += 1
        return count * 2
    
    """ ↗ 방향 대각선으로 인접한 돌의 갯수를 count하고, 갯수만큼의 가중치를 return """
    def checkSecondDiagonal(self, row, col, b):
        scoreList = [0.0, 3.0, 6.0, 10.0]
        
        count = 1
        emptySpace = 1
        for i in range(1, 6):
            if col + i < b.width:
                if row - i >= 0:
                    if b.data[row - i][col + i] is self.oppCh():
                        break
                    elif b.data[row - i][col + i] is ' ':
                        if emptySpace is 0:
                            break
                        emptySpace -= 1
                        count += 1
                    else: count += 1
                    
        emptySpace = 1
        for i in range(1, 6):
            if col - i >= 0:
                if row + i < b.height:
                    if b.data[row + i][col - i] is self.oppCh():
                        break
                    elif b.data[row + i][col - i] is ' ':
                        if emptySpace is 0:
                            break
                        emptySpace -= 1
                        count += 1
                    else: count += 1
        return count * 2
    
    """ 나의 돌이 아니거나 비어있는 공간인 경우 false를 리턴한다 """   
    def doNotNeedCheck(self, b, row, col):
        if b.data[row][col] == ' ':
            return True
        if self.oppCh() == b.data[row][col]: 
            return True
        return False

class Player_portall:
    """ an AI player for Connect Four """
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
        if(self.ox == 'X'):
            return 'O'
        else:
            return 'X'
        
    def scoreBoard(self, b):
        oppOX = self.oppCh()
        if(b.winsFor(self.ox) == True):
            return 100.0
        elif(b.winsFor(oppOX) == True):
            return 0.0
        else:
            return 50.0
        
    def getColumnWeight(self, b):
        weightList = [0] * b.width
        for index in range(0, b.width):
            if index <= b.width / 2: weightList[index] = weightList[index-1] + 2
            else: weightList[index] = weightList[index-1] - 2
        return weightList
    
    def calculateScore(self, b):
        score = 0
        weightList = self.getColumnWeight(b)
        for row in range(0, b.height):
            for col in range(0, b.width):
                if b.data[row][col] == self.ox:
                    score += weightList[col]
                elif b.data[row][col] == self.oppCh():
                    score -= weightList[col]
        return score
   
    def scoreBoardTourney(self, b):
        if b.winsFor(self.ox) == True:
            return 100.0
        elif b.winsFor(self.oppCh()) == True:
            return 0.0
        else:
            return 50 + self.calculateScore(b)            
                        
    def scoresFor(self, b):
        scoreList = [0.0] * b.width        
        for i in range(0, b.width):
            if (b.allowsMove(i) == False):
                scoreList[i] = -1.0
                continue
            elif(self.ply == 0):
                scoreList[i] = self.scoreBoardTourney(b)
                scoreList[i] += self.checkContinuousPlayer(b, self.getCurrentRow(b, i), i, self.oppCh())
            else:
                b.addMove(i, self.ox)
                oppPlayer = Player(self.oppCh(), self.tbt, self.ply - 1)
                preList = oppPlayer.scoresFor(b)
                preList = self.moveMinMax('max', preList)
                if 100.0 in preList or len(preList) == 0: scoreList[i] = 0.0
                else: scoreList[i] = 100 - preList[0]
                scoreList[i] += self.checkContinuousPlayer(b, self.getCurrentRow(b, i), i, self.oppCh())
                b.delMove(i)
        return scoreList  

    def tiebreakMove(self, scores):
        maxValue = max(scores);
        if (self.tbt == 'LEFT'):
            for i in range(0, len(scores)):
                if maxValue == scores[i]:
                    return i
        elif (self.tbt == 'RIGHT'):
            for i in range(len(scores), 0, -1):
                if maxValue == scores[i - 1]:
                    return i - 1
        else:
            maxIndexList = []
            for i in range(0, len(scores)):
                if scores[i] == maxValue:
                    maxIndexList.append(i)        
            randomColumn = random.sample(maxIndexList, 1).pop()
            return randomColumn   
                
    def nextMove(self, b):
        scoreList = self.scoresFor(b)
        print scoreList
        maxMove = self.tiebreakMove(scoreList)
        return maxMove
    
    def moveMinMax(self, kind, scoreList):        
        if kind == 'max': 
            scoreList.sort(reverse=True)
        else: 
            scoreList.sort()
            for index in range(0, len(scoreList)):
                if -1.0 in scoreList: scoreList.remove(-1.0)
        return scoreList
    
    def getCurrentRow(self, b, index):
        # 해당 인덱스에서 몇번째 row에 수를 놓았는지를 알아낸다.
        row = b.height - 1
        while(row >= 0):
            if(b.data[row][index] == ' '):
                return row
            row -= 1
        return 0
    
    def checkContinuousPlayer(self, b, row, index, player):
        colScore = 0
        # 주변에 적들이 얼마나 많이 있는지를 체크
        for gap in range(0, 4):
            colScore += self.getCountOfAroundColumn(b, row, index, gap, player)
        return colScore
    
    def getCountOfAroundColumn(self, b, row, index, gap, player):
        score = 0
        # 가로(오른쪽)
        if(index + gap < b.width and b.data[row][index + gap] == player):
            score += gap
        # 가로(왼쪽)
        if(index - gap >= 0 and b.data[row][index - gap] == player):
            score += gap
        # 세로(위)
        if(row - gap >= 0 and b.data[row - gap][index] == player):
            score += gap 
        # 세로(아래)
        if(row + gap < b.height and b.data[row + gap][index] == player):
            score += gap  
        # 대각선(위)
        if(row - gap >= 0):
            if(index - gap >= 0 and b.data[row - gap][index - gap] == player):
                score += gap
            if(index + gap < b.width and b.data[row - gap][index + gap] == player):
                score += gap
        # 대각선(아래)
        if(row + gap < b.height):
            if(index - gap >= 0 and b.data[row + gap][index - gap] == player):
                score += gap
            if(index + gap < b.width and b.data[row + gap][index + gap] == player):
                score += gap
        return score


class Player1(object):
   
    def __init__(self, pawn, tbt, ply):
        self.pawn = pawn
        self.tbt = tbt
        self.ply = ply
        #self.weightColumn = [20.0,30.0,40.0,50.0,40.0,30.0,20.0]
        
    def __repr__(self):
        s = "Player for " + self.ox + "\n"
        s += " with tiebreak type: " + self.tbt + "\n"
        s += " and ply == " + str(self.ply) + "\n\n"
        return s
        
    def oppCh(self):
        if(self.pawn is 'X'):
            return 'O'
        else:
            return 'X'
    
    def scoreBoard(self, board):
        if(board.winsFor(self.oppCh())):
            return 0.0;
        elif(board.winsFor(self.pawn)):
            return 100.0
        else:
            return 50.0

    # 자신의 말이 2개, 3개, 4개일 경우 가중치를 부여, 계산합니다.
    # 상대의 말이 4개일 경우, 음수의 가중치를 부여, 계산합니다.
    # 가로, 세로, positive diagonal, negative diagonal 총 4개의 방향을 체크합니다.

    # 향후 개선사항
    # 현재까지의 진행사항은 자신의 연속된 말이 있는 모든 경우에 대해 가중치를 부여, 계산하고 있으나,
    # 향후에는 연속된 말이 있으며, 내가 놓을 공간이 있을 경우에 한하여 가중치를 부여 할 예정입니다.
    # 또한, 현재 상대의 말이 4개일 경우에 대해서만 음수의 가중치를 부여, 계산하고 있으나
    # 2, 3개의 경우에도 가중치를 부여, 내 가중치와 상대의 가중치를 비교하여 최적화된 가중치를 반환하도록 할 예정입니다.
    def scoreBoard4Tourney(self, board):
        #print "l"
        if(board.winsFor(self.pawn)):
            return 1000.0
        elif(board.winsFor(self.oppCh())):
            return -1000.0;

        elif(self.checkForStreak(board, self.pawn, 2)>=1 or self.checkForBetween(board, self.pawn) >=1):
            return 250.0
        elif(self.checkForStreak(board, self.oppCh(), 2)>=1 or self.checkForBetween(board, self.oppCh())>=1):
            return -250.0
        elif(self.checkForStreak(board, self.pawn, 3)>=1 or  self.checkForBetweenFour(board, self.pawn)>=1):
            return 500.0
        elif(self.checkForStreak(board, self.oppCh(), 3)>=1 or self.checkForBetweenFour(board, self.oppCh())>=1):
            return -500.0
#         elif(self.checkForStreak(board, self.pawn, 1)>=1):
#             return 100.0
#         elif(self.checkForStreak(board, self.oppCh(), 1)>=1):
#             return -100.0
        else:
            return 50.0
        
    def checkForStreak(self, board, pawn, streak):        
        count = 0.0        
        for i in range(board.height):            
            for j in range(board.width):     
                if board.data[i][j] == pawn:
                    count += self.verticalStreak(i, j, board, streak)                                       
                    count += self.horizontalStreak(i, j, board, streak)                                        
                    count += self.diagonalCheck(i, j, board, streak)        
#         print "count =", count
        return count                
    
    def verticalStreak(self, row, col, board, streak):        
        consecutiveCount = 0.0        
        for i in range(row, board.height):            
            if board.data[i][col] == board.data[row][col]:                
                consecutiveCount += 1.0            
            else:                
                break            
            
        if consecutiveCount >= streak:
            return 1.0      
        else:            
            return 0.0      
            
    def horizontalStreak(self, row, col, board, streak):        
        consecutiveCount = 0.0       
        for j in range(col, board.width):            
            if board.data[row][j] == board.data[row][col]:                
                consecutiveCount += 1.0            
            else:                
                break        
            
        if consecutiveCount >= streak:            
            return 1.0        
        else:            
            return 0.0      
            
    def diagonalCheck(self, row, col, board, streak):        
        total = 0.0                
        consecutiveCount = 0.0        
        j = col        
        for i in range(row, board.height):            
            if j > board.height:                
                break            
            elif board.data[i][j] == board.data[row][col]:                
                consecutiveCount += 1            
            else:                
                break            
            
            j += 1 # increment column when row is incremented                    
            
        if consecutiveCount >= streak:            
                total += 1.0        # check for diagonals with negative slope        
        
        consecutiveCount = 0.0        
        j = col        
        for i in range(row, -1, -1):            
            if j > board.height:                
                break            
            elif board.data[i][j] == board.data[row][col]:                
                consecutiveCount += 1.0          
            else:                
                break            
            
            j += 1 # increment column when row is incremented        
            
        if consecutiveCount >= streak:            
                total += 1.0        
        
        return total     

    
    
    def checkForBetween(self, board, pawn):        
        count = 0.0        
        count += self.horizentalBetween(board, pawn)
        count += self.diagonalBetween(board, pawn)
        return count                
    
    def horizentalBetween(self, board, pawn):        
        between_count = 0.0       
        for i in range(board.height):
            for j in range(1, board.width-1):            
                if board.data[i][j-1] == pawn and board.data[i][j+1] == pawn:                
                    between_count += 1.0            

            
          
        return between_count      
            
    def diagonalBetween(self, board, pawn):        
        between_count = 0.0       
        for i in range(1, board.height-1):
            for j in range(1, board.width-1):            
                if board.data[i-1][j-1] == pawn and board.data[i+1][j+1] == pawn:          
                    between_count += 1.0            

          
        for i in range(board.height-2, 0, -1):            
            for j in range(1, board.width-1):   
                if board.data[i-1][j+1] == pawn and board.data[i+1][j-1] == pawn:          
                    between_count += 1.0           
        
        return between_count
    
    def checkForBetweenFour(self, board, pawn):        
        count = 0.0        
        count += self.horizentalBetweenFour(board, pawn)
        count += self.diagonalBetweenFour(board, pawn)
        return count                
    
    def horizentalBetweenFour(self, board, pawn):        
        between_count = 0.0       
        for i in range(board.height):
            for j in range(1, board.width-2):            
                if board.data[i][j-1] == pawn and board.data[i][j+1] == pawn and board.data[i][j+2]:                
                    between_count += 1.0            
        
        for i in range(board.height):
            for j in range(2, board.width-1):            
                if board.data[i][j-1] == pawn and board.data[i][j-2] == pawn and board.data[i][j+1]:                
                    between_count += 1.0
            
          
        return between_count      
            
    def diagonalBetweenFour(self, board, pawn):        
        between_count = 0.0       
        for i in range(1, board.height-2):
            for j in range(1, board.width-2):            
                if board.data[i-1][j-1] == pawn and board.data[i+1][j+1] == pawn and board.data[i+2][j+2] == pawn:          
                    between_count += 1.0            
        
        for i in range(2, board.height-1):
            for j in range(2, board.width-1):            
                if board.data[i-1][j-1] == pawn and board.data[i+1][j+1] == pawn and board.data[i-2][j-2] == pawn:          
                    between_count += 1.0            
          
        for i in range(board.height-3, 0, -1):            
            for j in range(1, board.width-2):   
                if board.data[i-1][j+1] == pawn and board.data[i+1][j-1] == pawn and board.data[i-2][j+2] == pawn:          
                    between_count += 1.0   
                            
        for i in range(board.height-2, 1, -1):            
            for j in range(2, board.width-1):   
                if board.data[i-1][j+1] == pawn and board.data[i+1][j-1] == pawn and board.data[i+2][j-2] == pawn:          
                    between_count += 1.0   
        
        return between_count          
        
    def tiebreakMove(self, scores):

        #if(self.ply%2 == 0):
        #    for i in range(len(scores)):
        #        scores[i] = -(scores[i])
        if(self.pawn == 'X'):
            weightColumn = [20.0,30.0,40.0,50.0,40.0,30.0,20.0] 
        elif(self.pawn == 'O'):
            weightColumn = [20.0,30.0,40.0,40.0,40.0,30.0,20.0]
            
        for index in range(len(scores)):
            if scores[index] != -100000.0 :
                scores[index] += weightColumn[index]
        #print self.pawn, " = ",scores
        maxindices = self.getHighestScoreIndex(scores)
        
        if(self.tbt is 'LEFT'):
            return maxindices[0];
        elif(self.tbt is 'RIGHT'):
            return maxindices[len(maxindices) - 1]
        else:
            return random.choice(maxindices)

    
    def getHighestScoreIndex(self, scores):
        maxValue = max(scores)
        maxIndices = []
        for i in range(len(scores)):
            if(scores[i] == maxValue):
                maxIndices.append(i)
        
        return maxIndices

    def getBoardScore(self, op_scorelist):
        if (max(op_scorelist) == 0.0):
            value = 100.0
        elif (max(op_scorelist) == 100.0):
            value = 0.0
        else:
            value = 50.0

        return value
    
    def scoresFor(self, board):
        boardScores = [-999.0] * board.width
        
        for i in range(len(boardScores)):
            
            if(board.allowsMove(i) is False):
                boardScores[i] = -100000.0

            elif(board.winsFor(self.pawn)):
                boardScores[i] = 1000.0
                break
            elif(self.ply == 0):
                #print board
                boardScores[i] = self.scoreBoard4Tourney(board)
                #print boardScores[i], i
                #time.sleep(0.1)
            else:
                board.addMove(i, self.pawn)
                
                if(board.isFull()):
                    boardScores[i] = 0.0
                    
                elif board.winsFor(self.pawn):
                    boardScores[i] = 1000.0
                    board.delMove(i)
                    continue
#                 elif board.winsFor(self.oppCh()):
#                     boardScores[i] = -1000.0
#                     board.delMove(i)
#                     continue
                else:
                    #print board
                    current_op = Player1(self.oppCh(), self.tbt, self.ply - 1)
                    op_scorelist = current_op.scoresFor(board)
                    #print self.pawn, " = ", op_scorelist, "ply = ", self.ply, "column = ", i
                    boardScores[i] = -max(op_scorelist)
                board.delMove(i)
       # print self.pawn, " = ", boardScores, " ply = ", self.ply
        return boardScores

        
    def nextMove(self, board):
        return self.tiebreakMove(self.scoresFor(board))
       
       
    def isGameOver(self, board):
        if(self.checkForStreak(board, self.pawn, 4) >= 1):
            return True
        elif(self.checkForStreak(board, self.oppCh(), 4) >= 1):
            return True
#         elif(board.isFull()):
#             return True
        else:
            return False

class Player18(object):
    
    def __init__(self, ox, tbt, ply):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply
        self.boardPriority = [0.01, 0.02, 0.03, 0.04, 0.03, 0.02, 0.01]
        self.initTurn = True

    def __repr__(self):
        """ creates an appropriate string """
        s = "Players for " + self.ox + "\n"
        s += " with tiebreak type: " + self.tbt + "\n"
        s += " and ply == " + str(self.ply) + "\n\n"
        return s
    
    def oppCh(self):
        if (self.ox == 'X') : return 'O'
        else : return 'X'
    
    def scoreBoard(self, b):
        if (b.winsFor(self.ox)):
            return 100.0
        elif (b.winsFor(self.oppCh())):
            return 0.0
        else: 
            return 50.0 
    
    def scoreBoard4Tourney(self, b):
        strategyScore = self.scoreBoard(b)
        
        if (self.isWinsFor(strategyScore)):
            return strategyScore
        
        return strategyScore + self.checkForMyStrategyScore(b) - self.checkForOppStrategyScore(b)
       
    def checkForMyStrategyScore(self, b):
        myStrategyScore = 0.0
        for row in xrange(0, b.height):
            for col in xrange(0, b.width):
                if b.data[row][col] == self.ox:
                    myStrategyScore += self.checkForStrategyScore(b, row, col, self.ox)
                    myStrategyScore += self.checkForStrategyScore(b, row, col, self.oppCh())
        return myStrategyScore
    
    def checkForOppStrategyScore(self, b):
        oppStrategyScore = 0.0
        for row in xrange(0, b.height):
            for col in xrange(0, b.width):
                if b.data[row][col] == self.oppCh():
                    oppStrategyScore += self.checkForStrategyScore(b, row, col, self.ox)
                    oppStrategyScore += self.checkForStrategyScore(b, row, col, self.oppCh())
        return oppStrategyScore
    
    # private function for scoreBoard4Tourney  
    def isWinsFor(self, strategyScore):
        return strategyScore == 100.0 or strategyScore == 0.0
    
    # private function for scoreBoard4Tourney
    def checkForStrategyScore(self, b, row, col, userType):
        strategyList = []
        
        strategyList.append(self.checkForLeft(b, row, col, userType))
        strategyList.append(self.checkForLeftUp(b, row, col, userType))
        strategyList.append(self.checkForLeftDown(b, row, col, userType))
        strategyList.append(self.checkForRight(b, row, col, userType))
        strategyList.append(self.checkForRightUp(b, row, col, userType))
        strategyList.append(self.checkForRightDown(b, row, col, userType))
        strategyList.append(self.checkForDown(b, row, col, userType))
        strategyList.append(self.checkForUp(b, row, col, userType))  
        return sum(strategyList)
    
    def checkForLeft(self, b, row, col, userType):
        check = 0.0
        
        if (col - 1 < 0):
            return check                
        if (b.data[row][col - 1] == userType):
            check += 2.0
            if (col - 2 < 0):
                return check
            if (b.data[row][col - 2] == userType):
                check += 4.0
                if (col - 3 < 0):
                    check -= 1.0
                    return check
                if (b.data[row][col - 3] == userType):
                    check += 5.0
        return check
    
    def checkForRight(self, b, row, col, userType):
        check = 0.0
        
        if (col + 1 >= b.width):
            return check                
        if (b.data[row][col + 1] == userType):
            check += 2.0
            if (col + 2 >= b.width):
                return check
            if (b.data[row][col + 2] == userType):
                check += 4.0
                if (col + 3 >= b.width):
                    check -= 1.0
                    return check
                if (b.data[row][col + 3] == userType):
                    check += 5.0
        return check
        
    def checkForLeftUp(self, b, row, col, userType):
        check = 0.0
        
        if (row - 1 < 0 or col - 1 < 0):
            return check
        if (b.data[row - 1][col - 1] == userType):
            check += 2.0
            if (row - 2 < 0 or col - 2 < 0):
                return check
            if (b.data[row - 2][col - 2] == userType):
                check += 4.0
                if (row - 3 < 0 or col - 3 < 0):
                    check -= 1.0
                    return check
                if (b.data[row - 3][col - 3] == userType):
                    check += 5.0
        return check
    
    def checkForRightUp(self, b, row, col, userType):
        check = 0.0
        
        if (row - 1 < 0 or col + 1 >= b.width):
            return check                
        if (b.data[row - 1][col + 1] == userType):
            check += 2.0
            if (row - 2 < 0 or col + 2 >= b.width):
                return check
            if (b.data[row - 2][col + 2] == userType):
                check += 4.0
                if (row - 3 < 0 or col + 3 >= b.width):
                    check -= 1.0
                    return check
                if (b.data[row - 3][col + 3] == userType):
                    check += 5.0
        return check 
    
    def checkForLeftDown(self, b, row, col, userType):
        check = 0.0
        
        if (row + 1 >= b.height or col - 1 < 0):
            return check                
        if (b.data[row + 1][col - 1] == userType):
            check += 2.0
            if (row + 2 >= b.height or col - 2 < 0):
                return check
            if (b.data[row + 2][col - 2] == userType):
                check += 4.0
                if (row + 3 >= b.height or col - 3 < 0):
                    check -= 1.0
                    return check
                if (b.data[row + 3][col - 3] == userType):
                    check += 5.0       
        return check  
    
    def checkForRightDown(self, b, row, col, userType):
        check = 0.0
        
        if (row + 1 >= b.height or col + 1 >= b.width):
            return check                
        if (b.data[row + 1][col + 1] == userType):
            check += 2.0
            if (row + 2 >= b.height or col + 2 >= b.width):
                return check
            if (b.data[row + 2][col + 2] == userType):
                check += 4.0
                if (row + 3 >= b.height or col + 3 >= b.width):
                    check -= 1.0
                    return check
                if (b.data[row + 3][col + 3] == userType):
                    check += 5.0
        return check
    
    def checkForDown(self, b, row, col, userType):
        check = 0.0 
        
        if (row + 1 >= b.height):
            return check                
        if (b.data[row + 1][col] == userType):
            check += 2.0
            if (row + 2 >= b.height):
                return check
            if (b.data[row + 2][col] == userType):
                check += 4.0
                if (row + 3 >= b.height):
                    check -= 1.0
                    return check
                if (b.data[row + 3][col] == userType):
                    check += 5.0
        return check
    
    def checkForUp(self, b, row, col, userType):
        check = 0.0
        
        if (row - 1 < 0):
            return check                
        if (b.data[row - 1][col] == userType):
            check += 2.0
            if (row - 2 < 0):
                return check
            if (b.data[row - 2][col] == userType):
                check += 4.0
                if (row - 2 < b.height):
                    check -= 1.0
                    return check
                if (b.data[row - 3][col] == userType):
                    check += 5.0
        return check
    
    def tiebreakMove(self, scores):
        maxValue = max(scores)
        if (self.tbt == 'LEFT'):
            return self.maxColumnToLeftLocation(scores, maxValue)
        elif (self.tbt == 'RIGHT'):
            return self.maxColumnToRightLocation(scores, maxValue)
        elif (self.tbt == 'CENTER'):
            return self.maxColumnToCenterLocation(scores, maxValue)
        else:
            return self.maxColumnToRandomLocation(scores, maxValue)
            
    # private function for tiebreakMove
    def maxColumnToLeftLocation(self, scores, maxValue):
        for leftIndex in xrange(0, len(scores)):
            if(scores[leftIndex] == maxValue):
                return leftIndex
    
    # private function for tiebreakMove
    def maxColumnToRightLocation(self, scores, maxValue):
        for rightIndex in xrange(len(scores)-1, -1, -1):
            if(scores[rightIndex] == maxValue):
                return rightIndex
    
    # private function for tiebreakMove (Using Random Function)
    def maxColumnToRandomLocation(self, scores, maxValue):
        maxIndices = []
        for Index in xrange(0, len(scores)):
            if(scores[Index] == maxValue):
                maxIndices.append(Index)
        return random.choice(maxIndices);
    
    # private function for tiebreakMove
    def maxColumnToCenterLocation(self, scores, maxValue):
        maxIndices = []
        for leftIndex in xrange(0, len(scores)):
            if(scores[leftIndex] == maxValue):
                maxIndices.append(leftIndex)
        if (len(maxIndices) == 1):
            return maxIndices[0]
        return maxIndices[len(maxIndices)/2];
    
    def scoresFor(self, b):
        if b.winsFor(self.oppCh()): # base case 2
            return [0] * b.width
        
        scores = [50]*b.width     
        for col in xrange(0, b.width) :
            if not(b.allowsMove(col)): # base case 1
                scores[col] = -1.0
                continue 
         
            if self.ply == 0: # base case 3
                scores[col] = self.scoreBoard4Tourney(b)
                continue
            
            b.addMove(col, self.ox)
            oppScores = Player18(self.oppCh(), self.tbt, self.ply-1).scoresFor(b)
            
            oppMax = max(oppScores) - self.boardPriority[col]
            scores[col] = 100.0 - oppMax
            
#             print col, ' : ', scores
#             print ' opp : ' , oppScores
#             print b
            b.delMove(col)
        return scores
    
    def nextMove(self, b):
        scores = self.scoresFor(b)
        print scores
        return self.tiebreakMove(scores)

player = Player18('X', 'RANDOM', 3)
human = Player_PP('O', 'RANDOM', 4)

sc = scoreCounter()

for x in xrange(50):
    b = Board(7,6)
    b.playGame(player, human, sc)

print "Owin:" + str(sc.oWinCount) + "   "+ "Xwin:" + str(sc.xWinCount)
