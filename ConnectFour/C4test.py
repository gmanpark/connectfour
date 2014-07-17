import unittest

from C4 import Board
from C4 import Player

class Test(unittest.TestCase):
    
    def setUp(self):
        self.board = Board(7, 6)
        
    def testSetBoard(self):
        board = Board(2, 2)
        board.setBoard('0011')
        
        outputBoard = '|O|O|' + '\n' + \
                      '|X|X|' + '\n' + \
                      '-----' + '\n' + \
                      ' 0 1'
        self.assertEqual(board.__repr__(), outputBoard)

    def testBoardRepresentation(self):
        board = Board(7, 6)
        
        outputBoard = '| | | | | | | |' + '\n' + \
                      '| | | | | | | |' + '\n' + \
                      '| | | | | | | |' + '\n' + \
                      '| | | | | | | |' + '\n' + \
                      '| | | | | | | |' + '\n' + \
                      '| | | | | | | |' + '\n' + \
                      '---------------' + '\n' + \
                      ' 0 1 2 3 4 5 6'
        self.assertEqual(board.__repr__(), outputBoard)
        
    def testAllowMove(self):
        board = Board(2, 2)
        board.addMove(0, 'X')
        board.addMove(0, 'O')
        
        self.assertEqual(board.allowsMove(-1), False)
        self.assertEqual(board.allowsMove(0), False)
        self.assertEqual(board.allowsMove(1), True)
        self.assertEqual(board.allowsMove(2), False)

    def testIsFullTwoByTwo(self):
        board = Board(2, 2)
        self.assertEqual(board.isFull(), False)
        board.setBoard('0011')
        self.assertEqual(board.isFull(), True)
        
    def testIsFullSevenBySix(self):
        self.board.clear();
        self.assertEqual(self.board.isFull(), False)
        
        self.board.setBoard('000000111111322222233333444444655555566666')
        
        outputBoard = '|O|O|X|O|O|X|O|' + '\n' + \
                      '|X|X|O|X|X|O|X|' + '\n' + \
                      '|O|O|X|O|O|X|O|' + '\n' + \
                      '|X|X|O|X|X|O|X|' + '\n' + \
                      '|O|O|X|O|O|X|O|' + '\n' + \
                      '|X|X|O|X|X|O|X|' + '\n' + \
                      '---------------' + '\n' + \
                      ' 0 1 2 3 4 5 6'

        self.assertEqual(self.board.__repr__(), outputBoard)
        self.assertEqual(self.board.isFull(), True)
        
    def testIsClear(self):
        compareBoard = Board(7, 6)
        
        compareBoard.setBoard('000000111111322222233333444444655555566666')
        
        # comparing fullBoard and emptyBoard
        self.assertNotEqual(self.board.__repr__(), compareBoard.__repr__())
        
        compareBoard.clear()              
        
        self.assertEqual(self.board.__repr__(), compareBoard.__repr__())
        
    def testDelMove(self):
        compareBoard = Board(7, 6)
        
        compareBoard.setBoard('0')
        
        # comparing fullBoard and emptyBoard
        self.assertNotEqual(self.board.__repr__(), compareBoard.__repr__())
        
        compareBoard.delMove(0)              
        
        self.assertEqual(self.board.__repr__(), compareBoard.__repr__())
        
    def testAddMove_put_value_in_full_row(self):
        board = Board(2, 2)
        board.addMove(1, 'O')
        board.addMove(1, 'X')
        self.assertEqual(board.addMove(1, 'O'), None)
        
    def testSelectedColByPointX(self):
        
        self.assertEqual(self.board.getSelectedCol(67), 0)
        self.assertEqual(self.board.getSelectedCol(126), 1)
        self.assertEqual(self.board.getSelectedCol(180), 2)
        self.assertEqual(self.board.getSelectedCol(246), 3)
        self.assertEqual(self.board.getSelectedCol(308), 4)
        self.assertEqual(self.board.getSelectedCol(369), 5)
        self.assertEqual(self.board.getSelectedCol(425), 6)
        
    def testChangeChecker(self):
        self.assertEqual(self.board.changeChecker('X'), 'O')
        self.assertEqual(self.board.changeChecker('O'), 'X')
        self.assertNotEqual(self.board.changeChecker('X'), 'X')
        self.assertNotEqual(self.board.changeChecker('O'), 'O')
        
    def testVerticalXwin(self):
        '''
        | | | | | | |X|
        | | | | |X|O|X|
        | | | | |X|O|X|
        |O| | | |X|O|X|
        |O| | | |O|X|O|
        |O| | | |X|O|X|
        ---------------
         0 1 2 3 4 5 6
        '''
        self.board.clear()
        self.board.setBoard('6544564560456045606')
        self.isXwin()
        
        '''
        |X| | | | | | |
        |X|O| | | | | |
        |X|O| | | | | |
        |X|O| | | | | |
        |O|X| | | | | |
        |X|O|X|O| | | |
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('0120130101010')
        self.isXwin()

        '''
        | | | | | | | |
        | | | | | | | |
        |X| | | | | | |
        |X| | | | | | |
        |X| |O| | | | |
        |X|O|O| | | | |
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('0102020')
        self.isXwin()
        
         
        '''
        | | | | | | | |
        | | | | | | | |
        | | | | | | |X|
        | | | | | | |X|
        | | | | |O| |X|
        | | | |O|O|O|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('65646364')
        self.isXwin()
        
        '''
        | | | | | | | |
        | | | | | | | |
        | | | | |X| | |
        | | | | |X| | |
        |O|O| | |X| | |
        |O|O|O| |X|X|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('40516240414')
        self.isXwin()
        
        '''
        | | | | | | | |
        | | | | | | | |
        | | |X| | | | |
        | | |X|O|X|O| |
        | | |X|O|X|O| |
        | | |X|O|X|O| |
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('2345234523452')
        self.isXwin()

    def testHorizontalXwin(self):
        '''
        | | | | | | | |
        | | | | | | | |
        | | | | | | | |
        | | | | | | | |
        |O|O| | | | | |
        |O|O| |X|X|X|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('60514031')
        self.isXwin()
        
        
        '''
        | | | | | | | |
        | | | | | | | |
        | | | | | | | |
        | | | | | | | |
        |O| | | | | | |
        |X|X|X|X| |O|O|
        ---------------
         0 1 2 3 4 5 6
        '''
        self.board.clear()
        self.board.setBoard('0615203')
        self.isXwin()
        
        '''
        | | | | | | | |
        | | | | | | | |
        | | | | | | | |
        |O| |X|X|X|X| |
        |O| |X|O|X|O| |
        |O| |X|O|X|O| |
        ---------------
         0 1 2 3 4 5 6
        '''
        self.board.clear()
        self.board.setBoard('234523452030405')
        self.isXwin()

    def testHorizontalOwin(self):
        '''
        |O|O|O|O|X|X|X|
        |O|X|O|X|O|X|O|
        |X|O|X|O|X|O|X|
        |X|O|X|O|X|O|X|
        |O|X|O|X|O|X|O|
        |X|O|X|O|X|O|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('654321065432106543210563412600123451605243')
        self.isOwin()
        
        '''
        | |X|X|O|O|O|O|
        |O|X|O|X|O|X|O|
        |X|O|X|O|X|O|X|
        |X|O|X|O|X|O|X|
        |O|X|O|X|O|X|O|
        |X|O|X|O|X|O|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('654321065432106543210563412600123456152413')
        self.isOwin()
        
        '''
        | | | | | | | |
        | | | | | | | |
        | | | | | | | |
        | | | | | | | |
        | | | | |X| | |
        |O|O|O|O|X|X|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('40516243')
        self.isOwin()
        
        
    def testDiagonalFromRightToLeftOwin(self):
        '''
        |O|X|O| | | | |
        |X|O|X| | | | |
        |O|X|O| | | | |
        |X|O|X|O| |X| |
        |O|X|O|O| |X|O|
        |X|O|X|X| |O|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('00000061111115222222365353')
        self.isOwin()
    
        '''
        |X|O|O|O|X|O|X|
        |O|X|X|X|O|X|O|
        |X|O|O|O|X|O|X|
        |X|O|X|O|X|O|X|
        |O|X|O|X|O|X|O|
        |X|O|X|O|X|O|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('012345665432100123456111000222444333666555')
        self.isOwin()
        
    def testDiagonalFromRightToLeftXwin(self):
        '''
        | | | | | | | |
        | | | | | | | |
        | | | |X| | | |
        | | | |O|X|O|X|
        | | | |X|O|X|O|
        | | | |O|X|O|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.setBoard('6546546543333')
        self.isXwin()
        '''
        | | | |X| | | |
        | | | |X|X| | |
        | | | |O|O|X|O|
        | | | |X|X|O|X|
        |O|O| |O|O|X|O|
        |O|X| |X|X|O|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('66664444455550333013313')
        self.isXwin()
        
        '''
        | | | | | | | |
        | | | | | | | |
        |X| | | | | | |
        |O|X| | | | | |
        |O|O|X|X| | | |
        |O|O|X|X| | | |
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('30312021100')
        self.isXwin()
        
        '''
        |X|O|O| | | | |
        |X|X|X| | | | |
        |O|O|X| | | | |
        |O|X|O|X| | | |
        |X|O|X|O| | | |
        |X|O|X|O| | | |
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('012301233012211021020')
        self.isXwin()
        
        '''
        | | | |X| | | |
        | | | |X|X| | |
        | | | |O|O|X|O|
        | | | |O|X|O|X|
        | | | |X|O|X|O|
        | | | |X|O|X|O|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('3456345665435443363')
        self.isXwin()
        
    def testDiagonalFromLeftToRightOwin(self):
        '''
        | | | |O| | | |
        | | |O|O| | | |
        | |O|X|O| | |X|
        |O|X|X|X| | |X|
        |X|X|O|O| | |X|
        |X|O|X|O| | |O|
        ---------------
         0 1 2 3 4 5 6
        '''
        self.board.clear()
        self.board.setBoard('0123122336630011226363')
        self.isOwin()
        
        '''
        | | | | | | | |
        | | | | | | | |
        | | | | | |X|O|
        | | | |O|X|O|X|
        | | | |X|O|X|O|
        | | | |O|X|O|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('65465465433356')
        self.isOwin()
        
        '''
        | | | | | |O|O|
        | | | | |O|X|O|
        | | | |O|X|X|X|
        | | |O|O|X|O|X|
        | | |X|X|O|X|O|
        |X|X|O|O|X|O|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('65465465433343546655061222')
        self.isOwin()
        
    def testDiagonalFromLeftToRightXwin(self):
        '''
        | | | | | | |X|
        | | | | | |X|O|
        | | | | |X|O|X|
        |O| | |X|X|O|X|
        |O|X| |X|O|X|O|
        |O|O| |O|X|O|X|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.setBoard('65465465433030455061166')
        self.isXwin()
        
        '''
        | | | | | | | |
        | | | | | | | |
        | | | |X| | | |
        | | |X|X| | | |
        | |X|O|O| | | |
        |X|O|O|X| | |O|
        ---------------
         0 1 2 3 4 5 6
         '''
        self.board.clear()
        self.board.setBoard('01123223363')
        self.isXwin()

    def isXwin(self):
        self.assertEquals(self.board.winsFor('O'), False)
        self.assertEquals(self.board.winsFor('X'), True)

    def isOwin(self):
        self.assertEquals(self.board.winsFor('O'), True)
        self.assertEquals(self.board.winsFor('X'), False)


    # C4 Class Test

    def test_oppCh(self):
        p = Player('X', 'LEFT', 3)
        self.assertEquals(p.oppCh(), 'O')

        p = Player('O', 'LEFT', 0)
        self.assertEquals(p.oppCh(), 'X')

    def test_scoreBoard(self):
        b = Board(7,6)
        b.setBoard('01020305')
        p = Player('X', 'LEFT', 0)
        self.assertEquals(p.scoreBoard(b), 100.0)
        p = Player('O', 'LEFT', 0)
        self.assertEquals(p.scoreBoard(b), 0.0)
        p = Player('O', 'LEFT', 0)
        self.assertEquals(p.scoreBoard(Board(7,6)), 50.0)

    def test_tiebreakMove(self):
        scores = [0, 0, 50, 0, 50, 50, 0]
        p = Player('X', 'LEFT', 1)
        p2 = Player('X', 'RIGHT', 1)
        self.assertEquals(p.tiebreakMove(scores), 2)
        self.assertEquals(p2.tiebreakMove(scores), 5)

    def test_scoresFor(self):
        b = Board(7,6)
        b.setBoard('1211244445')
        self.assertEquals(Player('X', 'LEFT', 0).scoresFor(b), [50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0])
        self.assertEquals(Player('O', 'LEFT', 1).scoresFor(b), [50.0, 50.0, 50.0, 100.0, 50.0, 50.0, 50.0])
        self.assertEquals(Player('X', 'LEFT', 2).scoresFor(b), [0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 0.0])
        self.assertEquals(Player('X', 'LEFT', 3).scoresFor(b), [0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0])
        self.assertEquals(Player('O', 'LEFT', 3).scoresFor(b), [50.0, 50.0, 50.0, 100.0, 50.0, 50.0, 50.0])
        self.assertEquals(Player('O', 'LEFT', 4).scoresFor(b), [0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0])

    def test_nextMove(self):
        b = Board(7,6)
        b.setBoard('1211244445')
        self.assertEquals(Player('X', 'LEFT', 1).nextMove(b), 0)
        self.assertEquals(Player('X', 'RIGHT', 1).nextMove(b), 6)
        self.assertEquals(Player('X', 'LEFT', 2).nextMove(b), 3)
        self.assertEquals(Player('X', 'RIGHT', 2).nextMove(b), 3)
        self.assertEquals(Player('X', 'RANDOM', 2).nextMove(b), 3)


if __name__ == "__main__":    
    unittest.main()

