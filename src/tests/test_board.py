#! /usr/bin/env python

'''
Tests for the Board class and it's helpers
'''

import os
import sys

from unittest import TestCase
from board import Board, BoardException, calc_winner


class TestBoard(TestCase):
    def test_load(self):
        board = Board()
        board.load('xoxoxoxox')
        self.assertEquals(str(board), '''\
                      1   2   3
                        |   |   
                 A    x | o | x 
                        |   |   
                     ---+---+---
                        |   |   
                 B    o | x | o 
                        |   |   
                     ---+---+---
                        |   |   
                 C    x | o | x 
                        |   |   
''')

        board.load('xo ox xo ')
        self.assertEquals(str(board), '''\
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
                 C    x | o |   
                        |   |   
''')

        with self.assertRaises(BoardException):
            board.load('') # too few chars
        with self.assertRaises(BoardException):
            board.load('xxxoooxxxo') # too many chars
        with self.assertRaises(BoardException):
            board.load('Axxoooxxx') # wrong chars


    def test_open_spots(self):
        board = Board()
        board.load('         ')
        self.assertEquals( range(9), list(board.open_spots()))

        board.load('xxo   oox')
        self.assertEquals( [3,4,5], list(board.open_spots()))

        board.load('xxoooxoox')
        self.assertEquals( [], list(board.open_spots()))


    def test_place_piece(self):
        board = Board()
        board.place_piece('x',0)

        with self.assertRaises(BoardException):
            board.place_piece('A',0)


    def test_calc_winner(self):
        board = Board()
        board.load('         ')
        winner = calc_winner(board)
        self.assertEquals(None, winner)

        board.load('xxxo o o ')
        winner = calc_winner(board)
        self.assertEquals('x', winner)

        board.load(' x x xooo')
        winner = calc_winner(board)
        self.assertEquals('o', winner)


