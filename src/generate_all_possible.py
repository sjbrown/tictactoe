#! /usr/bin/env python

import os
import cPickle

from board import Board, calc_winner_or_tie
from collections import defaultdict

PICKLE_FILENAME = os.path.join(os.path.dirname(__file__), 'ttt.pkl')

memo_dict = {}

class Node(object):
    def __init__(self, board, parent=None):
        self.board = board
        self.children = []
        self.edges = []
        win_or_tie = calc_winner_or_tie(self.board)
        if win_or_tie:
            self.outcome = set([win_or_tie])
        else:
            self.outcome = set()

    def __eq__(self, other):
        return self.board.grid == other.board.grid

    def __repr__(self):
        return '<Node %s>' % self.board.dump()

    def calc_edges(self):
        for child in self.children:
            self.edges.append((child, child.outcome))
            self.outcome = self.outcome.union(child.outcome)

    def descend(self):
        if self.edges:
            return # already calculated
        for spot in self.board.open_spots:
            board = self.board.copy()
            board.place_piece(board.next_player, spot)
            if board in memo_dict:
                node = memo_dict[board]
            else:
                node = Node(board, self)
                memo_dict[board] = node
                node.descend()
            self.children.append(node)
        self.calc_edges()

def load_root():
    '''Loads the datastructure from a pickle file, 'ttt.pkl'.
    Takes about 30 seconds.
    '''
    fp = file(PICKLE_FILENAME, 'rb')
    root = cPickle.load(fp)
    fp.close()
    return root

def dump_root(root):
    '''Writes the datastructure to a pickle file, 'ttt.pkl'.
    Takes about 40 seconds.
    '''
    fp = file(PICKLE_FILENAME, 'wb')
    cPickle.dump(root, fp, protocol=-1)
    fp.close()

def make_root():
    '''Creates a datastructure with all possible tic tac toe boards.
    Takes about 5 minutes
    '''
    b = Board()
    b.load('         ')
    root = Node(b)
    root.descend()
    return root

def main():
    print "Cannot dump from main() because of http://bugs.python.org/issue5509"
    print "use generate_all_possible_dumper.py instead"

if __name__ == '__main__':
    main()
