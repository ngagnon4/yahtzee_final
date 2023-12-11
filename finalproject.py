''' 

THIS CODE WILL NOT RUN PROPERLY IF YOU DO NOT HAVE PYSIMPLEGUI INSTALLED

To install PySimpleGUI, please enter the following command into your computer's Terminal:

pip install pysimplegui

If this does not work, try the following:

pip3 install pysimplegui

'''


import random as r
import PySimpleGUI as gui

class Window():
    def __init__(self):
        gui.theme('BrightColors')
        ''' Sets all gui colorschemes'''


    def board_chooser(self):
        layout = [   [gui.Text('Choose your board: ')],
                     [gui.Text('Regular Board    |'), gui.Text('Odds & Evens    |'), gui.Text('Triple Chance')],
                     [gui.Text()],
                     [gui.Text('Regular Board: A traditional game of Yahtzee')],
                     [gui.Text('Odds and Evens: All lower scores will be scored by the total of the odd or even numbers')],
                     [gui.Text('Triple Chance: A traditional style of Yahtzee, but the chance score is tripled!')],
                     [gui.Text('')],
                     [gui.Text('Enter 1 for Regular, 2 for Odds & Evens, or 3 for Triple Chance')],
                     [gui.Input()],
                     [gui.Button('Choose Board')] ]
        ''' Creates all text displays and determines their orientation on the gui; 
        also declares what will be text, an input, or a button'''

        window = gui.Window('Yahtzee', layout)
        ''' Creates window '''

        while True:
            event, values = window.read()
            if event == 'Choose Board' or event == gui.WIN_CLOSED:
                break
        window.close()
        return values
    ''' closes window when button or x are pressed. returns value of what was input'''

    def window_roll(self, name, dice):
        layout = [  [gui.Text('{}'.format(name))],
                    [gui.Text("Enter the dice you'd like to reroll")],
                    [gui.Text('Your Dice')],
                    [gui.Text('D1: ' + str(dice.roll[0])),
                     gui.Text('D2: ' + str(dice.roll[1])), 
                     gui.Text('D3: ' + str(dice.roll[2])), 
                     gui.Text('D4: ' + str(dice.roll[3])), 
                     gui.Text('D5: ' + str(dice.roll[4]))],
                    [gui.Input()],
                    [gui.Button('Roll Dice!')],
                    [gui.Text('** Enter dice as numbers (ex. 134) **')] ]
        ''' Creates all text displays and determines their orientation on the gui; 
        also declares what will be text, an input, or a button'''

        window = gui.Window('Yahtzee!', layout)
        ''' creates window '''

        while True:
            event, values = window.read()
            if event == 'Roll Dice!' or event == gui.WIN_CLOSED:
                break
        window.close()
        return values
    ''' closes window when button or x are pressed. returns value of what was input'''

    def window_final_roll(self, name, dice):
        layout = [  [gui.Text('{}'.format(name))],
                    [gui.Text('Your Dice')],
                    [gui.Text('D1: ' + str(dice.roll[0])),
                     gui.Text('D2: ' + str(dice.roll[1])), 
                     gui.Text('D3: ' + str(dice.roll[2])), 
                     gui.Text('D4: ' + str(dice.roll[3])), 
                     gui.Text('D5: ' + str(dice.roll[4]))],
                    [gui.Button('Choose how to score')],    ]
        window = gui.Window('Yahtzee!', layout)
        while True:
            event, values = window.read()
            if event == 'Choose how to score' or event == gui.WIN_CLOSED:
                break
        window.close()
        return values
    
    ''' follows the same syntax as the above two methods'''
    
    def window_scorep1(self, dice):
        l = []
        layout = [[gui.Text("Available Moves: ")]]
        for key in game.p1board.movedict.keys():
            w = game.p1board.movedict[key]
            l.append((key, w))
        for move in l:
            layout.append([gui.Text(move)])

        ''' this for loop adds all available scoring methods to the layout list'''
        ''' a loop must be used since the move dictionary is dynamic '''

        layout.append([ [gui.Text('Your Dice:')],
                        [gui.Text('D1: ' + str(dice.roll[0])),
                        gui.Text('D2: ' + str(dice.roll[1])), 
                        gui.Text('D3: ' + str(dice.roll[2])), 
                        gui.Text('D4: ' + str(dice.roll[3])), 
                        gui.Text('D5: ' + str(dice.roll[4]))],
                       [gui.Input()], 
                       [gui.Button('Enter move')],])
        window = gui.Window('Yahtzee!', layout)
        while True:
            event, values = window.read()
            if event  == 'Enter move' or event == gui.WIN_CLOSED:
                break
        window.close()
        return values
    
    ''' follows the same syntax as above methods '''

    def window_scorep2(self, dice):
        l = []
        layout = []
        for key in game.p2board.movedict.keys():
            w = game.p2board.movedict[key]
            l.append((key, w))
        for move in l:
            layout.append([gui.Text(move)])
        layout.append([[gui.Text('D1: ' + str(dice.roll[0])),
                        gui.Text('D2: ' + str(dice.roll[1])), 
                        gui.Text('D3: ' + str(dice.roll[2])), 
                        gui.Text('D4: ' + str(dice.roll[3])), 
                        gui.Text('D5: ' + str(dice.roll[4]))],
                       [gui.Input()], 
                       [gui.Button('Enter move')],])
        window = gui.Window('Yahtzee!', layout)
        while True:
            event, values = window.read()
            if event  == 'Enter move' or event == gui.WIN_CLOSED:
                break
        window.close()
        return values
    
    ''' this is the same as the above method, but for player 2's board'''

class Dice():
    def __init__(self):
        self.roll = [r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6), r.randint(1,6)]
        ''' randomizes 5 6-sided die in a list '''

    def roll_dice(self, dice_list):
        for x in range(len(dice_list)):
            n = dice_list[x-1]
            self.roll[int(n)-1] = r.randint(1,6)
        return self
    ''' rolls the individual dice given in a list, returning the updated values of the 5 dice'''

class Board():
    def __init__(self):
        self.lowerscore = 0
        self.movelist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.movedict = {1: 'Ones', 2: 'Twos', 3: 'Threes', 4: 'Fours', 5: 'Fives', 6: 'Sixes', 7: 'Three of a Kind', 8: 'Four of a Kind', 9: 'Full House', 10: 'Small Straight', 11: 'Large Straight', 12: 'Yahtzee', 13: 'Chance'}
    ''' Declares and defines the moves and tracks the score of the first 6 scoring methods '''

    def movemaker(self, move, dice):
        if move == 1:
            return self.ones(dice)
        elif move == 2: 
            return self.twos(dice)
        elif move == 3:
            return self.threes(dice)
        elif move == 4:
            return self.fours(dice)
        elif move == 5:
            return self.fives(dice)
        elif move == 6:
            return self.sixes(dice)
        elif move == 7:
            return self.kind_3(dice)
        elif move == 8:
            return self.kind_4(dice)
        elif move == 9:
            return self.full_house(dice)
        elif move == 10:
            return self.small_straight(dice)
        elif move == 11:
            return self.large_straight(dice)
        elif move == 12:
            return self.yahtzee(dice)
        elif move == 13:
            return self.chance(dice)
        ''' when a move is entered in the game, this method executes the move and returns the score 
        dependening on the given move id number'''
        
    def ones(self, dice):
        score = 0
        for x in range(0,5):
            if dice.roll[x] == 1:
                score += 1
        return score
    
    def twos(self, dice):
        score = 0
        for x in range(0,5):
            if dice.roll[x] == 2:
                score += 2
        return score
    
    def threes(self, dice):
        score = 0
        for x in range(0,5):
            if dice.roll[x] == 3:
                score += 3
        return score
    
    def fours(self, dice):
        score = 0
        for x in range(0, 5):
            if dice.roll[x] == 4:
                score += 4
        return score
    
    def fives(self, dice):
        score = 0
        for x in range(0,5):
            if dice.roll[x] == 5:
                score += 5
        return score

    def sixes(self, dice):
        score = 0
        for x in range(0,5):
            if dice.roll[x] == 6:
                score += 6
        return score
    ''' Previous six methods are mostly self explanatory '''

    def kind_3(self, dice):
        score = 0
        l1 = ["1" for x in dice.roll if x == 1]
        l2 = ["2" for x in dice.roll if x == 2]
        l3 = ["3" for x in dice.roll if x == 3]
        l4 = ["4" for x in dice.roll if x == 4]
        l5 = ["5" for x in dice.roll if x == 5]
        l6 = ["6" for x in dice.roll if x == 6]
        if len(l1) >= 3 or len(l2) >= 3 or len(l3) >= 3 or len(l4) >= 3 or len(l5) >= 3 or len(l6) >= 3:
            score = sum(dice.roll)
        return score
    ''' puts each dice in a list depending on the die's number. takes the length of each list
    if any of the lists have three or more dice, the sum is taken of all dice'''

    def kind_4(self, dice):
        score = 0
        l1 = ["1" for x in dice.roll if x == 1]
        l2 = ["2" for x in dice.roll if x == 2]
        l3 = ["3" for x in dice.roll if x == 3]
        l4 = ["4" for x in dice.roll if x == 4]
        l5 = ["5" for x in dice.roll if x == 5]
        l6 = ["6" for x in dice.roll if x == 6]
        if len(l1) >= 4 or len(l2) >= 4 or len(l3) >= 4 or len(l4) >= 4 or len(l5) >= 4 or len(l6) >= 4:
            score = sum(dice.roll)
        return score
    ''' same as above method, but with a threshold of 4 dice rather than 3'''

    def full_house(self, dice):
        score = 0
        l1 = ["1" for x in dice.roll if x == 1]
        l2 = ["2" for x in dice.roll if x == 2]
        l3 = ["3" for x in dice.roll if x == 3]
        l4 = ["4" for x in dice.roll if x == 4]
        l5 = ["5" for x in dice.roll if x == 5]
        l6 = ["6" for x in dice.roll if x == 6]
        ''' this is the same list of dice method as the above two class methods '''
        if len(l1) == 3:
            if len(l2) ==2 or len(l3) == 2 or len(l4) == 2 or len(l5) == 2 or len(l6) == 2:
                score = 25
        elif len(l2) == 3:
            if len(l1) ==2 or len(l3) == 2 or len(l4) == 2 or len(l5) == 2 or len(l6) == 2:
                score = 25
        elif len(l3) == 3:
            if len(l2) ==2 or len(l1) == 2 or len(l4) == 2 or len(l5) == 2 or len(l6) == 2:
                score = 25
        elif len(l4) == 3:
            if len(l2) ==2 or len(l3) == 2 or len(l1) == 2 or len(l5) == 2 or len(l6) == 2:
                score = 25
        elif len(l5) == 3:
            if len(l2) ==2 or len(l3) == 2 or len(l4) == 2 or len(l1) == 2 or len(l6) == 2:
                score = 25
        elif len(l6) == 3:
            if len(l2) ==2 or len(l3) == 2 or len(l4) == 2 or len(l5) == 2 or len(l1) == 2:
                score = 25

            ''' checks if three of one dice are the same and two of another are the same '''
        else:
            return score
        return score
        
    
    def small_straight(self, dice):
        score = 0
        l1 = ["1" for x in dice.roll if x == 1]
        l2 = ["2" for x in dice.roll if x == 2]
        l3 = ["3" for x in dice.roll if x == 3]
        l4 = ["4" for x in dice.roll if x == 4]
        l5 = ["5" for x in dice.roll if x == 5]
        l6 = ["6" for x in dice.roll if x == 6]
        ''' same list of dice method '''
        if len(l1) != 0 and len(l2) != 0 and len(l3) != 0 and len(l4) != 0:
            score = 30
        elif len(l5) != 0 and len(l2) != 0 and len(l3) != 0 and len(l4) != 0:
            score = 30
        elif len(l6) != 0 and len(l5) != 0 and len(l3) != 0 and len(l4) != 0:
            score = 30
        else:
            return score
        return score
    ''' checks if four of the dice are in a row, ie 1,2,3,4 or 3,4,5,6 '''

    def large_straight(self, dice):
        score = 0
        l1 = ["1" for x in dice.roll if x == 1]
        l2 = ["2" for x in dice.roll if x == 2]
        l3 = ["3" for x in dice.roll if x == 3]
        l4 = ["4" for x in dice.roll if x == 4]
        l5 = ["5" for x in dice.roll if x == 5]
        l6 = ["6" for x in dice.roll if x == 6]
        if len(l1) != 0 and len(l2) != 0 and len(l3) != 0 and len(l4) != 0 and len(l5) != 0:
            score = 40
        elif len(l6) != 0 and len(l2) != 0 and len(l3) != 0 and len(l4) != 0 and len(l5) != 0:
            score = 40
        else:
            return score
        return score
    ''' four dice must now be in a row '''
    
    def yahtzee(self, dice):
        score = 0
        yahtzeelist = ["0" for x in dice.roll if x == dice.roll[0]]
        if len(yahtzeelist) == 5:
            score = 50
        return score
    
    def chance(self, dice):
        return sum(dice.roll)
    
class Board_Lower(Board):
    def __init__(self):
        super().__init__()
        self.movedict = {1: 'Odds', 2: 'Evens', 3: 'Odds', 4: 'Evens', 5: 'Odds', 6: 'Evens', 7: 'Three of a Kind', 8: 'Four of a Kind', 9: 'Full House', 10: 'Small Straight', 11: 'Large Straight', 12: 'Yahtzee', 13: 'Chance'}
    
    ''' every 1-6 method is now an even or odd method '''

    def movemaker(self, move, dice):
        if move == 1 or move == 3 or move == 5:
            return self.odds(dice)
        elif move == 6 or move == 4 or move == 2:
            return self.evens(dice)
        elif move == 7:
            return self.kind_3(dice)
        elif move == 8:
            return self.kind_4(dice)
        elif move == 9:
            return self.full_house(dice)
        elif move == 10:
            return self.small_straight(dice)
        elif move == 11:
            return self.large_straight(dice)
        elif move == 12:
            return self.yahtzee(dice)
        elif move == 13:
            return self.chance(dice)
        
    def odds(self, dice):
        score = 0
        for x in dice.roll:
            if x == 1 or x == 3 or x == 5:
                score += x
        return score
    
    def evens(self, dice):
        score = 0
        for x in dice.roll:
            if x == 2 or x == 4 or x == 6:
                score += x
        return score
    
    def kind_3(self, dice):
        return super().kind_3(dice)
    
    def kind_4(self, dice):
        return super().kind_4(dice)
    
    def full_house(self, dice):
        return super().full_house(dice)
    
    def large_straight(self, dice):
        return super().large_straight(dice)
    
    def small_straight(self, dice):
        return super().small_straight(dice)
    
    def chance(self, dice):
        return super().chance(dice)
    
    def yahtzee(self, dice):
        return super().yahtzee(dice)
    
class Board_Triple_Chance(Board):
    def __init__(self):
        super().__init__()
    def movemaker(self, move, dice):
        return super().movemaker(move, dice)
    def ones(self, dice):
        return super().ones(dice)
    def twos(self, dice):
        return super().twos(dice)
    def threes(self, dice):
        return super().threes(dice)
    def fours(self, dice):
        return super().fours(dice)
    def fives(self, dice):
        return super().fives(dice)
    def sixes(self, dice):
        return super().sixes(dice)
    def kind_3(self, dice):
        return super().kind_3(dice)
    def kind_4(self, dice):
        return super().kind_4(dice)
    def full_house(self, dice):
        return super().full_house(dice)
    def large_straight(self, dice):
        return super().large_straight(dice)
    def small_straight(self, dice):
        return super().small_straight(dice)
    def yahtzee(self, dice):
        return super().yahtzee(dice)
    def chance(self, dice):
        score = super().chance(dice)
        return score * 3
    ''' chance is now tripled ''' 
    
class Game():
    scoresheet_number = 1
    def __init__(self):
        self.playernumber = 2
        self.playernames = []
        for player in range(1, self.playernumber+1):
            self.playernames.append(input("Player {}, what is your name? ".format(player)))
        print("\n\n\n\n")
        '''creates a game attribute of the two players names'''
        self.playerscores = {self.playernames[x]:0 for x in range(0,self.playernumber)}
        self.movenumber = 2

        board = Window.board_chooser(self)
        try:
            board = int(board[0])
        except(ValueError):
            print("Please enter either 1, 2, or 3")
            board = Window.board_chooser(self)
        except(TypeError):
            print("Please enter either 1, 2, or 3")
            board = Window.board_chooser(self)
        ''' runs board choosing gui, catching errors with invalid entries '''
        if board == 1:
            self.p1board = Board()
            self.p2board = Board()
        if board == 2:
            self.p1board = Board_Lower()
            self.p2board = Board_Lower()
        if board == 3:
            self.p1board = Board_Triple_Chance()
            self.p2board = Board_Triple_Chance()
        ''' designates the board attributes to the proper board type '''
    
    def how_to_play(self):
        print('Yahtzee is a game of rolling dice and scoring based on those rolls.\n'
              'You will have three chances to roll your dice and can choose which dice to reroll\n'
              'Once you are done rolling, you can choose how to score your turn:\n'
              '1-6: A sum of the dice with the same value of the method numer\n'
              '3 of a kind: A sum of all dice if three of the dice are the same number\n'
              '4 of a kind: The same as above, but four dice must be the same\n'
              'Full House: 3 dice must have the same number and 2 dice must have another that is the same\n'
              'Small Straight: Four numbers in a row, ie 1, 2, 3, 4\n'
              'Large Straight: All five numbers in a row, ie 1, 2, 3, 4, 5\n'
              'Yahtzee: All five dice are the same number\n'
              'Chance: The sum of all dice with no conditions\n\n'
              'All of these methods can only be used once. Once all methods are taken, final scores are tallied\n'
              'The highest scorer will win')

    def display_score(self):
        return(print(self.playerscores))
        
    def make_a_move(self):

        if self.movenumber % 2 == 0:
            print("{}, you're up!\n".format(self.playernames[0]))
            print(self.p1board.movedict)
            ''' Initial display: Name and move shown by system '''

            dice = Dice()
            roll = 0
            while roll < 2:
                print("\n")
                roll += 1
                dlist = Window.window_roll(self, self.playernames[0], dice)
                try:
                    dice.roll_dice(dlist[0])
                except(ValueError):
                    print('Input must be a number representing dice being rolled')
                    dlist = Window.window_roll(self, self.playernames[0], dice)
                    dice.roll_dice(dlist[0])
                ''' Creates a dice object and rolls it twice 
                    a check is created for invalid entries on dice to be rerolled
                    calls the gui to take inputs for which dice to reroll
                '''

            Window.window_final_roll(self, self.playernames[0], dice) 
            ''' This displays the final roll, does not accept inputs '''

            move = Window.window_scorep1(self, dice)
            try:
                move = int(move[0])
                ''' attempts to execute a move as prompted by the window '''
                while move <0:
                    print('Move must be represented as a positive integer')
                    move = Window.window_scorep1(self, dice)
                    move = int(move[0])
                    ''' Value check for whether the move is represented properly'''

            except(ValueError):
                print('Move must be represented as a number')
                move = Window.window_scorep1(self, dice)
                move = int(move[0])
                ''' Asks for the move again if not represented properly '''
                while move <0:
                    print('Move must be represented as a positive integer')
                    move = Window.window_scorep1(self, dice)
                    move = int(move[0])
                    ''' Another catch for improper number '''

            if move not in self.p1board.movelist:
                print("Move not available. Which move will you make? ")
                move = Window.window_scorep1(self, dice)
                move = int(move[0])
                ''' A check for if the move is not in the range of possible moves '''

            self.playerscores[self.playernames[0]] += self.p1board.movemaker(move, dice)
            ''' This adds the value returned by movemaker to the players score '''

            if move in range(1,7):
                self.p1board.lowerscore += self.p1board.movemaker(move, dice)
            ''' This adds the value of the score to the lower score checker '''

            if 12 not in self.p1board.movelist:
                if self.p1board.movemaker(12, dice) == 50:
                    self.playerscores[self.playernames[0]] += 50
            ''' This adds an extra 50 points to the players score if they score yahtzee more than once '''
            self.p1board.movelist.remove(move)
            ''' Removes the move made from the list of remaining moves '''
            del self.p1board.movedict[move]
            ''' Deletes the move from the dictionary of moves '''
            self.movenumber += 1
            ''' Increases movenumber to change it to the next players turn '''
            print("\n\n\n\n\n\n")
            return self.playerscores[self.playernames[0]]
            ''' returns an updated score '''
        
        else:
            ''' THE FOLLOWING CODE IS THE EXACT SAME AS ABOVE, BUT FOR PLAYER 2 '''

            print("{}, you're up!\n".format(self.playernames[1]))
            print(self.p2board.movedict)
            dice = Dice()
            roll = 0
            while roll < 2:
                print("\n")
                roll += 1
                dlist = Window.window_roll(self, self.playernames[1], dice)
                try:
                    dice.roll_dice(dlist[0])
                except(ValueError):
                    print('Input must be a number representing dice being rolled')
                    dlist = Window.window_roll(self, self.playernames[1], dice)
                    dice.roll_dice(dlist[0])
            Window.window_final_roll(self, self.playernames[1], dice)
            move = Window.window_scorep2(self, dice)
            try:
                move = int(move[0])
                while move <0:
                    print('Move must be represented as a positive integer')
                    move = Window.window_scorep1(self, dice)
                    move = int(move[0])
            except(ValueError):
                print('Move must be represented as a number')
                move = Window.window_scorep1(self, dice)
                move = int(move[0])
                while move <0:
                    print('Move must be represented as a positive integer')
                    move = Window.window_scorep1(self, dice)
                    move = int(move[0])
            if move not in self.p2board.movelist:
                print("Move not available. Which move will you make? ")
                move = Window.window_scorep2(self, dice)
                move = int(move[0])
            self.playerscores[self.playernames[1]] += self.p2board.movemaker(move, dice)
            if move in range(1,7):
                self.p2board.lowerscore += self.p2board.movemaker(move, dice)
            if 12 not in self.p2board.movelist:
                if self.p2board.movemaker(12, dice) == 50:
                    self.playerscores[self.playernames[1]] += 50
            self.p2board.movelist.remove(move)
            del self.p2board.movedict[move]
            self.movenumber += 1
            print("\n\n\n\n\n\n")
            return self.playerscores[self.playernames[1]]
        
        
    def get_winner(self):
        if self.p1board.lowerscore >= 63:
            print("{}, 1 through 6 score bonus reached! 35 points added to your score.".format(self.playernames[0]))
            self.playerscores[self.playernames[0]] += 35
            ''' This adds 35 points to the players score if they met the proper lower score value '''
        if self.p2board.lowerscore >= 63:
            print("{}, 1 through 6 score bonus reached! 35 points added to your score.".format(self.playernames[1]))
            self.playerscores[self.playernames[1]]
            ''' Same as above, but for player 2 '''
        print(self.playerscores)
        if self.playerscores[self.playernames[0]] > self.playerscores[self.playernames[1]]:
            print("{}, you win!!".format(self.playernames[0]))
        else:
            print("{}, you win!!".format(self.playernames[1]))
        ''' This prints the winner of the game after checking the two scores '''

    def file_writer(self):
        Game.scoresheet_number += 1
        with open('pythonyahtzee.txt', 'at') as file:
            file.write('Scores for Game ' + str(Game.scoresheet_number) + ': \n')
            file.write(str(game.playerscores))
            file.write('\n -----------------------------------------------\n')


        
    def play_game(self):
        self.how_to_play()
        ''' Displays the how to play method after the game is initialized '''
        while self.p2board.movelist != []:
            self.display_score()
            self.make_a_move()
            ''' Displays the score and makes the next move until no moves are available '''
        self.file_writer()
        return self.get_winner()
        ''' Gets the winner at the end of the game '''

game = Game()
game.play_game()