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
        self.minmax_choice = None
        win_or_tie = calc_winner_or_tie(self.board)
        if win_or_tie:
            if win_or_tie == Board.x:
                self.best_x_outcome = 1
                self.best_o_outcome = -1
            elif win_or_tie == Board.o:
                self.best_x_outcome = -1
                self.best_o_outcome = 1
            else:
                self.best_x_outcome = 0
                self.best_o_outcome = 0
        else:
            self.best_x_outcome = None
            self.best_o_outcome = None

    def __eq__(self, other):
        return self.board.grid == other.board.grid

    def __repr__(self):
        return '<Node %s %s/%s>' % (self.board.dump(),
                                    self.best_x_outcome, self.best_o_outcome)

    def find_best_outcome_paths(self):
        if self.best_x_outcome != None:
            return
        if self.board.next_player == Board.x:
            self.best_x_outcome = max([i.best_x_outcome for i in self.children])
            self.best_o_outcome = min([i.best_o_outcome for i in self.children])
        else:
            self.best_o_outcome = max([i.best_o_outcome for i in self.children])
            self.best_x_outcome = min([i.best_x_outcome for i in self.children])
        worst_o_outcome = 1
        worst_x_outcome = 1
        for child in self.children:
            if self.board.next_player == Board.x:
                if child.best_o_outcome <= worst_o_outcome:
                    worst_o_outcome = child.best_o_outcome
                    self.minmax_choice = child
            else:
                if child.best_x_outcome <= worst_x_outcome:
                    worst_x_outcome = child.best_x_outcome
                    self.minmax_choice = child

    def descend(self):
        if self.best_x_outcome:
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
        self.find_best_outcome_paths()

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
