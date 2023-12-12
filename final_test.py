import unittest as test
from finalproject import Dice, Board, Game, Board_Lower, Window

class Dice_Test(test.TestCase):
    def test_basic(self):
        dice = Dice()
        self.assertEqual(len(dice.roll), 5)
        ''' Tests that 5 dice are stored in a list upon initialization '''
        dice.roll = [1,2,3,4,5]
        dice.roll_dice([1,3,5])
        self.assertNotEqual(dice.roll, [1,2,3,4,5])
        ''' Tests that roll_dice actually changes the dice '''
        self.assertEqual(dice.roll[1], 2)
        self.assertEqual(dice.roll[3], 4)
        ''' Tests that the two dice not rerolled remain the same '''

class Board_Test(test.TestCase):
    def test_scores_lower(self):
        dice = Dice()
        dice.roll = [1,1,1,2,2]
        self.assertEqual(Board.ones(self, dice), 3)
        self.assertEqual(Board.twos(self, dice), 4)
        dice.roll = [3,3,5,5,5]
        self.assertEqual(Board.fives(self, dice), 15)
        self.assertEqual(Board.threes(self,dice), 6)
        dice.roll = [6,6,4,4,6]
        self.assertEqual(Board.fours(self, dice), 8)
        self.assertEqual(Board.sixes(self, dice), 18)
        ''' These six tests test that all lower score items are returning scores properly '''

    def test_scores_upper(self):
        dice = Dice()
        dice.roll = [1,2,3,4,6]
        self.assertEqual(Board.small_straight(self,dice), 30)
        self.assertNotEqual(Board.large_straight(self,dice), 40)
        dice.roll = [1,2,3,4,5]
        self.assertEqual(Board.small_straight(self,dice)+10, Board.large_straight(self,dice))
        ''' Tests that small and large straight score properly '''
        dice.roll = [1,1,1,1,1]
        self.assertEqual(Board.yahtzee(self,dice), 50)
        self.assertEqual(Board.chance(self,dice), 5)
        ''' Tests Yahtzee and Chance scores '''
        self.assertEqual(Board.full_house(self,dice), 0)
        ''' Tests full house requires two different matching dice numbers '''
        dice.roll = [4,4,4,4,6]
        self.assertEqual(Board.kind_4(self,dice), 22)
        self.assertEqual(Board.kind_4(self,dice), Board.kind_3(self,dice))
        ''' Tests functionality of 3 / 4 of a kind'''
    
class Odd_Even_Board_Test(test.TestCase):

    def test_odds_evens(self):
        dice = Dice()
        dice.roll = [2,4,6,3,1]
        self.assertEqual(Board_Lower.odds(self,dice), 4)
        self.assertEqual(Board_Lower.evens(self,dice), 12)

class Game_Test(test.TestCase):
    
    def test_initialization(self):
        game = Game()
        ''' MUST ENTER NAMES AS Nick AND Noah'''
        self.assertEqual(game.playernames[0], 'Nick')
        self.assertEqual(game.playernames[1], 'Noah')
        ''' Name Test '''

class Window_Test(test.TestCase):
    
    def test_window(self):
        ''' MUST CHOOSE BOARD ONE '''
        ''' TESTS IF VALUES ARE RETURNED BY GUI '''
        values = Window.board_chooser(self)
        self.assertEqual(values[0], '1')



test.main()