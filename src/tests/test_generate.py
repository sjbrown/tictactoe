#! /usr/bin/env python

'''
Tests for the Node class and it's associates
'''

import os
import sys

from unittest import TestCase
from board import Board
import generate_all_possible
from generate_all_possible import Node



class TestNode(TestCase):
    def test_constructor(self):
        board = Board()
        board.load('ooxxxo   ')
        root = Node(board)

        self.assertEquals(root.children, [])
        self.assertEquals(root.best_x_outcome, None)

    def test_descend(self):
        board = Board()
        board.load('ooxxxo   ')
        root = Node(board)

        root.descend()

        b1 = Board()
        b1.load('ooxxxoo  ')
        c1 = Node(b1)
        b2 = Board()
        b2.load('ooxxxo o ')
        c2 = Node(b2)
        b3 = Board()
        b3.load('ooxxxo  o')
        c3 = Node(b3)
        expected = [c1, c2, c3]

        self.assertEquals(root.children, expected)

    def test_leaf_nodes(self):
        b = Board()
        b.load('ooxxxox  ')
        root = Node(b)

        root.descend()

        self.assertEquals(root.best_x_outcome, 1)
        self.assertEquals(root.best_o_outcome, -1)
        self.assertEquals(root.minmax_choice, None)

        b = Board()
        b.load('oooxx    ')
        root = Node(b)

        root.descend()

        self.assertEquals(root.best_x_outcome, -1)
        self.assertEquals(root.best_o_outcome, 1)
        self.assertEquals(root.minmax_choice, None)

    def test_minmax(self):
        # Game with a clear winner
        b = Board()
        b.load('oo xx    ')
        root = Node(b)
        root.descend()

        self.assertEquals(root.board.next_player, 'o')

        b1 = Board()
        b1.load('oooxx    ')
        node1 = Node(b1)

        self.assertEquals(root.minmax_choice, node1)

        # Tie game
        b = Board()
        b.load('ooxxxoo  ')
        root = Node(b)
        root.descend()

        self.assertEquals(root.board.next_player, 'x')
        self.assertEquals(root.best_x_outcome, 0)
        self.assertEquals(root.best_o_outcome, 0)

