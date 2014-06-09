#! /usr/bin/env python

class BoardException(Exception): pass

class Board(object):
    x = 'x'
    o = 'o'
    letters = [x,o]

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

    def load(self, nine_chars):
        '''load a tic-tac-toe board from a compact string of 9 chars'''

        if len(nine_chars) != 9:
            raise BoardException('Must be 9 chars')
        if not set(nine_chars).issubset(set('xo ')):
            raise BoardException("Must be x's, o's and ' ' chars")

        self.grid = list(nine_chars)

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
