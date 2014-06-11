#! /usr/bin/env python

class BoardException(Exception): pass

# A decorator for Board methods
def validate_after(orig_fn):
    def new_fn(self, *args, **kwargs):
        orig_fn(self, *args, **kwargs)
        self.validate()
    return new_fn

class Board(object):
    x = 'x'
    o = 'o'
    blank = ' '
    letters = [x,o]
    possible_values = [x,o,blank]

    def __init__(self):
        self.grid = [' ', ' ', ' ',
                     ' ', ' ', ' ',
                     ' ', ' ', ' ',
                    ]

    def __getitem__(self, index):
        return self.grid[index]

    def __str__(self):
        the_board = '''\
                      1   2   3
                        |   |   
                 A    %s | %s | %s 
                        |   |   
                     ---+---+---
                        |   |   
                 B    %s | %s | %s 
                        |   |   
                     ---+---+---
                        |   |   
                 C    %s | %s | %s 
                        |   |   
'''
        return the_board % tuple(self.grid)

    def validate(self):
        '''Some non-comprehensive validation for a Board'''
        if len(self.grid) != 9:
            raise BoardException('Must be 9 chars')
        if not set(self.grid).issubset(set(Board.possible_values)):
            raise BoardException("Must be x's, o's and ' ' chars")

    @validate_after
    def load(self, nine_chars):
        '''load a tic-tac-toe board from a compact string of 9 chars'''
        self.grid = list(nine_chars)

    def dump(self):
        return ''.join(self.grid)

    def copy(self):
        b = Board()
        b.load(self.dump())
        return b

    @property
    def next_player(self):
        exes = [i for i in self.grid if i == 'x']
        ohs = [i for i in self.grid if i == 'o']
        if len(ohs) > len(exes):
            return 'x'
        else:
            return 'o'

    @property
    def open_spots(self):
        for i in range(len(self.grid)):
            if self.grid[i] == ' ':
                yield i

    def place_piece(self, letter, spot):
        '''Return a new Board with the piece placed in this spot'''
        grid_copy = self.grid[:]
        if grid_copy[spot] != Board.blank:
            raise BoardException('Spot already taken')
        grid_copy[spot] = letter
        b = Board()
        b.load(''.join(grid_copy))
        return b

def calc_winner(board):
    '''Given a board, return the winner.
    returns either 'x', 'o', or None (if no winner)
    '''
    runs = [ (0,1,2), (3,4,5), (6,7,8), #horizontal
             (0,3,6), (1,4,7), (2,5,8), #vertical
             (0,4,8), (2,4,6) ]         #diagonal

    for letter in Board.letters:
        for a,b,c in runs:
            if letter == board[a] == board[b] == board[c]:
                return letter

    return None

def calc_winner_or_tie(board):
    '''Returns:
       either 'x', 'o', if one of those players has won.
       'tie' if the game is over and it's a tie game
       None if the game is not over
    '''
    winner = calc_winner(board)
    if winner == None and not list(board.open_spots):
        return 'tie'
    return winner



if __name__ == '__main__':
    b = Board()
    assert str(b) == '''\
                      1   2   3
                        |   |   
                 A      |   |   
                        |   |   
                     ---+---+---
                        |   |   
                 B      |   |   
                        |   |   
                     ---+---+---
                        |   |   
                 C      |   |   
                        |   |   
'''
    b.grid = [ 'x', 'o', ' ',
               'o', 'x', ' ',
               'o', ' ', 'x']
    assert str(b) == '''\
                      1   2   3
                        |   |   
                 A    x | o |   
                        |   |   
                     ---+---+---
                        |   |   
                 B    o | x |   
                        |   |   
                     ---+---+---
                        |   |   
                 C    o |   | x 
                        |   |   
'''
