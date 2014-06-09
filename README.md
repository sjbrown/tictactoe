tictactoe
=========

Tic Tac Toe Implementation Exercise

Developer's Log
===============


June 9

Ok, so the task is to create an implementation of Tic Tac Toe that satisfies:
 * one user can play against the computer
 * the computer will never lose

On the first point, that sounds easy enough.  A simple terminal interface
will suffice - just print out the current state of the board and ask the user
which row/column to put his next move.  Maybe an intro asking if the human
or the computer should go first, and a "Try again?" prompt at the end

----

    Welcome to sjbrown's Tic Tac Toe thingy!
    Would you like to go first (you play as o's) or let the computer go
    first (you play as x's)?
    
    type "me" if you would like to go first > _

----

    Current board state:
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

    type the row and column you would like to place your next piece > _

----
    
                        |   |   
                      X |   |   
                        |   |   
                     ---+---+---
                        |   |   
                      O | X |   
                        |   |   
                     ---+---+---
                        |   |   
                        | O | X 
                        |   |   

    The computer won!
    Would you like to play again?
    
    type "y" to play again > _
    
----

On the second point:
Having played my share of tic-tac-toe in childhood, I know that there is indeed
a never-losing strategy.

The search space for tic-tac-toe is fairly small, and since the requirements
do not specify that eg, larger grids may be a future requirement.

There are 9 grid spaces and 3 possible values (blank, x, o) for each, so the
max possible boards is 3^9.  If we store them all in a single file, it would be
about 172kb. And that would be with lots of superfluous content - board states
that could never be reached.

So let's see if there's a file online somewhere with all the possible legal
board states...
