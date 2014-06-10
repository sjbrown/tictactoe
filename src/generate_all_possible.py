#! /usr/bin/env python

from board import Board, calc_winner_or_tie
from collections import defaultdict

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

def main():
    b = Board()
    print b
    print list(b.open_spots)

if __name__ == '__main__':
    main()
