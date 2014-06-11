#! /usr/bin/env python

from itertools import cycle

import board
import generate_all_possible as gap

PLEASE_WAIT = '''\
    Please wait as the Artificial Intelligence loads.

    This should take approximately 30 seconds, depending on the speed
    and available memory of your computer...
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
    '''Artificial Intelligence'''
    def __init__(self):
        self.root = gap.load_root()

    def get_move(self, cur_board):
        node = gap.memo_dict[cur_board.dump()]
        next_node = node.minmax_choice
        return next_node.board

def rowcol_to_spot(rowcol):
    '''Turn a user input like "a1" or "b2" into an index like 0 or 4'''
    row = rowcol[0]
    col = rowcol[1]
    spot = 0
    spot += 'abc'.index(row) * 3
    spot += int(col) - 1
    return spot

def get_human_move(cur_board):
    while True:
        acceptable_input = False
        print '    Current board state:'
        print cur_board
        print ''
        while not acceptable_input:
            choice = raw_input(MOVE_PROMPT)
            choice = choice.lower()
            acceptable_input = ( len(choice) == 2
                                 and choice[0] in 'abc'
                                 and choice[1] in '123')
        try:
            spot = rowcol_to_spot(choice)
            b = cur_board.place_piece(cur_board.next_player, spot)
            break
        except Exception as e:
            color_message = "\033[1;33m"+ e.message +"\033[0m"
            print color_message
            print ''

    return b

def mainloop(ai, initial_board):
    b = initial_board

    choice = raw_input(INTRO_PROMPT)

    # who goes first, cpu or human?
    if choice.lower() == 'me':
        move_fns = cycle([get_human_move, ai.get_move])
    else:
        move_fns = cycle([ai.get_move, get_human_move])

    while board.calc_winner_or_tie(b) == None:
        move_fn = move_fns.next()
        b = move_fn(b)
        print ''
        print b
        print ''

    win_or_tie = board.calc_winner_or_tie(b)
    if win_or_tie == 'x':
        winner_msg = 'Winner is Xs!'
    elif win_or_tie == 'o':
        winner_msg = 'Winner is Os!'
    else:
        winner_msg = 'Tie Game!'
    print "Game over.", winner_msg
    print b
    print "Great Game!"

def main():
    print PLEASE_WAIT
    try:
        ai = AI()
    except IOError as e:
        print 'The AI file has not been generated yet.'
        print 'Please run the following command:'
        print ''
        print ' python generate_all_possible_dumper.py'
        print ''
        return

    print INTRO
    stop = False

    while not stop:
        print ''
        b = board.Board()
        b.load('         ') # initialize blank board
        mainloop(ai, b)
        print ''
        should_stop = raw_input(' type "y" to play again > ')
        if should_stop.lower() != 'y':
            stop = True


if __name__ == '__main__':
    main()
