#! /usr/bin/env python

class Board(object):
    def __init__(self):
        self.grid = [' ', ' ', ' ',
                     ' ', ' ', ' ',
                     ' ', ' ', ' ',
                    ]

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
