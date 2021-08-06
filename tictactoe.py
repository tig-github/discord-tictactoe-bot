#Tic Tac Toe program
import discord
from discord.ext import commands


"""
Player class, which handles the turns of each player, and initializing of the other two classes.
"""
class Player:
    def __init__(self):
        self.gameboard = Gameboard()
        self.gamelist = self.gameboard.gamelist
        self.win = Win()
        pass

    """
    Turn1 method which retrieves the command information (shaving the << off of the <<num response), checks if the square is valid using the initialized gamelist, and
    then assigns the value and builds the board using the new data. Returns the built board and a win_check to check the gamestate.
    """
    def turn1(self, choice):
        choiced = int(choice[2])
        if self.gamelist[choiced - 1] == 0:
            self.gamelist[choiced - 1] = 2
        else:
            print('square already taken')
            return False

        self.gameboard.assign_square()
        return self.win.win_check(self.gamelist), self.gameboard.build_board()


    def turn2(self, choice):
        choiced = int(choice[2])
        if self.gamelist[choiced - 1] == 0:
            self.gamelist[choiced - 1] = 5
        else:
            print('square already taken')
            return False

        self.gameboard.assign_square()
        return self.win.win_check(self.gamelist), self.gameboard.build_board()



"""
Class win that checks for the various win conditions, initializes each method as a possible dimensional win condition
"""
class Win:
    def win_check(self, gamelist):
        win_horz = self.win_check_horizontal(gamelist)
        if win_horz == False:
            return win_horz

        win_vert = self.win_check_vertical(gamelist)
        if win_vert == False:
            return win_vert

        win_dia = self.win_check_diagonal(gamelist)
        if win_dia == False:
            return win_dia

        tie = self.tie_check(gamelist)
        if tie == True:
            return tie

    """
    Checks for wins on horizontal rows of the board. For all checks, 6 represents a player 1 win and 15 represents a player 2 win, as the player 1 number is 2 making 2x3=6,
    whereas the player 2 number is 5 making 3x5=15. The reason 2 and 5 were chosen is they were the closest still differentiable numbers with sums that dont conflict, unlike
    2 and 3 where a row of two 3s would trigger a win condition
    """
    def win_check_horizontal(self, gamelist):
        if (gamelist[0] + gamelist[1] + gamelist[2]) == 6:
            print('player one wins')
            return False
        elif (gamelist[0] + gamelist[1] + gamelist[2]) == 15:
            print('player two wins')
            return False

        if (gamelist[3] + gamelist[4] + gamelist[5]) == 6:
            print('player one wins')
            return False
        elif (gamelist[3] + gamelist[4] + gamelist[5]) == 15:
            print('player two wins')
            return False

        if (gamelist[6] + gamelist[7] + gamelist[8]) == 6:
            print('player one wins')
            return False
        elif (gamelist[6] + gamelist[7] + gamelist[8]) == 15:
            print('player two wins')
            return False


    """
    Checks for wins on vertical columns of the board
    """
    def win_check_vertical(self, gamelist):
        if (gamelist[0] + gamelist[3] + gamelist[6]) == 6:
            print('player one wins')
            return False
        elif (gamelist[0] + gamelist[3] + gamelist[6]) == 15:
            print('player two wins')
            return False

        if (gamelist[1] + gamelist[4] + gamelist[7]) == 6:
            print('player one wins')
            return False
        elif (gamelist[1] + gamelist[4] + gamelist[7]) == 15:
            print('player two wins')
            return False

        if (gamelist[2] + gamelist[5] + gamelist[8]) == 6:
            print('player one wins')
            return False
        elif (gamelist[2] + gamelist[5] + gamelist[8]) == 15:
            print('player two wins')
            return False

    """
    Checks for wins on diagonals of the board
    """
    def win_check_diagonal(self, gamelist):
        if (gamelist[0] + gamelist[4] + gamelist[8]) == 6:
            print('player one wins')
            return False
        elif (gamelist[0] + gamelist[4] + gamelist[8]) == 15:
            print('player two wins')
            return False

        if (gamelist[2] + gamelist[4] + gamelist[6]) == 6:
            print('player one wins')
            return False
        elif (gamelist[2] + gamelist[4] + gamelist[6]) == 15:
            print('player two wins')
            return False

    """
    Checks if all values are full after win conditions are checked for, ie tie condition
    """
    def tie_check(self, gamelist):
        if 0 not in gamelist:
            print('tie')
            return True



"""
Gameboard class, which initializes the square attributes of the gameboard and a gamelist that handles win conditions and the assigning of a new board. Squares are initialized
as empty.
"""
class Gameboard:
    def __init__(self):
        self.gamelist = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.square_1 = '   '
        self.square_2 = '   '
        self.square_3 = '   '
        self.square_4 = '   '
        self.square_5 = '   '
        self.square_6 = '   '
        self.square_7 = '   '
        self.square_8 = '   '
        self.square_9 = '   '

    """
    Assigns each square with an X or an O depending on the inputted number-can make this way more efficient with a list or something simple
    """
    def assign_square(self):
        if self.gamelist[0] == 2:
            self.square_1 = ' X '
        if self.gamelist[1] == 2:
            self.square_2 = ' X '
        if self.gamelist[2] == 2:
            self.square_3 = ' X '
        if self.gamelist[3] == 2:
            self.square_4 = ' X '
        if self.gamelist[4] == 2:
            self.square_5 = ' X '
        if self.gamelist[5] == 2:
            self.square_6 = ' X '
        if self.gamelist[6] == 2:
            self.square_7 = ' X '
        if self.gamelist[7] == 2:
            self.square_8 = ' X '
        if self.gamelist[8] == 2:
            self.square_9 = ' X '

        if self.gamelist[0] == 5:
            self.square_1 = ' O '
        if self.gamelist[1] == 5:
            self.square_2 = ' O '
        if self.gamelist[2] == 5:
            self.square_3 = ' O '
        if self.gamelist[3] == 5:
            self.square_4 = ' O '
        if self.gamelist[4] == 5:
            self.square_5 = ' O '
        if self.gamelist[5] == 5:
            self.square_6 = ' O '
        if self.gamelist[6] == 5:
            self.square_7 = ' O '
        if self.gamelist[7] == 5:
            self.square_8 = ' O '
        if self.gamelist[8] == 5:
            self.square_9 = ' O '

    """
    Builds the board as a simple string containing the values and some builders, returns the string to be outputted
    """
    def build_board(self):
        gameboard_top = '#' + self.square_1 + '|' + self.square_2 + '|' + self.square_3 + '\n'
        gameboard_middle = '#' + self.square_4 + '|' + self.square_5 + '|' + self.square_6 + '\n'
        gameboard_bottom = '#' + self.square_7 + '|' + self.square_8 + '|' + self.square_9
        gameboard_edge = '#--+--+--\n'

        gameboard = gameboard_top + gameboard_edge + gameboard_middle + gameboard_edge + gameboard_bottom
        return gameboard
