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
        for row in range(0, h):
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
        
    def playGame(self, px, po):
        print("Welcome to Connect Four!\n")
        print(self)
        
        isWins = False
        checker = 'X'
        
        while self.isFull() == False:            
            print("\n" + checker + "'s choice:"),
            
            if checker is 'X':
                users_col = px.nextMove(b)
            else:
                users_col = po.nextMove(b)
                
            print(str(users_col) + "\n")
            
            if self.allowsMove(users_col) == False:
                continue
            
            self.addMove(users_col, checker)
            
            print(self)
            
            isWins = self.winsFor(checker)
            if isWins == True:
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

    def scoreBoard4Tourney(self, b):
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
                b.addMove(index, self.ox
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
                b.addMove(index, self.ox
                                opponent = Player(self.oppCh(), "RANDOM", self.ply - 1)
                oppScore = opponent.scoresFor(b)
                oppMax = max(oppScore)
                numericScores[index] = 100 - oppMax;
                b.delMove(index)
        return numericScores

    def nextMove(self, b):
        return self.tiebreakMove(self.scoresFor(b))
    
    
# b = Board(7, 6)
# b.setBoard( '1211244445' )
# print(b)
# 
# p = Player( 'X', 'LEFT', 0 )
# print(p.scoreBoard(b))
# 
# print(Player('O', 'LEFT', 0).scoreBoard(b))
# 
# print(Player('O', 'LEFT', 0).scoreBoard( Board(7,6) ))
# 
# 
# 
# scores = [0, 0, 50, 0, 50, 50, 0]
# p = Player('X', 'LEFT', 1)
# p2 = Player('X', 'RIGHT', 1)
# p3 = Player('X', 'RANDOM', 1)
# 
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

px = Player('X','LEFT',3)
po = Player2('O','LEFT',0)
b = Board(7,6)
b.playGame(px, po)


