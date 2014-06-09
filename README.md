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

So let's google to see if there's a file online somewhere with all the possible 
legal board states...

----

June 9

Trying to find a list of all possible board states has come up with nothing.

Interestingly, many of the search results point to Minmax as an algorithm for 
writing tic-tac-toe. AI.  I am skeptical if it is a good fit.  Tic-tac-toe is
such a small search space that there would be no sense in a depth limit, and
the values would all be +infinity, 0, and -infinity...

Anyway...

Ok, so let's reason it out.  What is an illegal board state?
 * Any state where (# of x's) > (# of o's)
 * Any state where (# of o's) > (# of x's) + 1
 * Any state where there is more than one 3-in-a-row
 * Any state where there is a 3-in-a-row of o's, and (# of o's) == (# of x's)

I think that's comprehensive.  
Ok, so we could generate all board states with code and prune all of 
the above... and then what?

After that we would find all the winning and tie states, and then create a 
directed graph from one state to another.  If there were weighted edges, the
AI would just lookup what state the board was currently in, and follow the
edge with the highest value.  Borrowing from Minmax, we could weight the edges
with 1, 0, and -1.

But if that's the datastructure I'm going to build, it seems silly to
brute-force all possibilities, and then prune.  I might as well write code
to build up a tree constrained by legal moves, and when it gets to an endgame
state (a leaf), it would check the winner or tie, and write that onto it's
edge.  Now that I think of it, it would be more clear if the weights were
'x', 0, and 'o', rather than 1, 0, -1.
