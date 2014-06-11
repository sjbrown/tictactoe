#! /usr/bin/env python

import board
import generate_all_possible as gap

PLEASE_WAIT = '''\
    Please wait as the Artificial Intelligence loads.

    This should take approximately 30 seconds, depending on the speed
    and available memory of your computer.
'''
INTRO = '''\
    Welcome to sjbrown's Tic Tac Toe thingy!
    Use Ctrl-C at any time to exit.
    Would you like to go first (you play as o's) or let the computer go
    first (you play as x's)?

'''
INTRO_PROMPT = '''\
 type "me" if you would like to go first, or just press Enter > '''
MOVE_PROMPT = '''\
 (Use Ctrl-C at any time to exit.)
 type the row and column you would like to place your next piece
 (for example, "a1") > '''


class AI(object):
    def __init__(self):
        self.root = gap.load_root()

    def get_move(self, cur_board):
        node = gap.memo_dict[cur_board.dump()]
        next_node = node.minmax_choice
        return next_node.board

def rowcol_to_spot(rowcol):
    row = rowcol[0]
    col = rowcol[1]
    spot = 0
    spot += 'abc'.index(row) * 3
    spot += int(col) - 1
    return spot

def get_human_move(cur_board):
    print '    Current board state:'
    print cur_board
    print ''
    acceptable_input = False
    while not acceptable_input:
        choice = raw_input(MOVE_PROMPT)
        acceptable_input = ( len(choice) == 2
                             and choice[0] in 'abc'
                             and choice[1] in '123')
    try:
        cur_board.place_piece(cur_board.next_player, rowcol_to_spot(choice))
    except:
        print 'FIX THIS'

    return cur_board

def main():
    print PLEASE_WAIT
    ai = AI()

    b = board.Board()
    b.load('         ')

    print INTRO
    choice = raw_input(INTRO_PROMPT)

    if not choice.lower() == 'me':
        b = ai.get_move(b)

    while board.calc_winner_or_tie(b) == None:
        b = get_human_move(b)
        print ''
        print b
        print ''
        if board.calc_winner_or_tie(b) == None:
            b = ai.get_move(b)

    print b
    print "DONE"


if __name__ == '__main__':
    main()
