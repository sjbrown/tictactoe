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

        self.assertEquals(root.edges, [])
        self.assertEquals(root.outcome, set())

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

