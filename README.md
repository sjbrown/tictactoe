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

----

June 9

Ok, now that I've written a little bit of the graph-manipulating part, I 
understand the purpose of using the Minmax approach.

It is not sufficient to just identify a board state and say "from here, there
exists a path to a board state where Player 1 wins", because expert play by
Player 2 may prevent us from reaching that state.  So we need to annotate the
edges not with "what states are possible?", but rather, for every edge:
 * the best result for Player 1 if Player 2 plays perfectly
 * the best result for Player 2 if Player 1 plays perfectly

----

June 11

Back to this project.  It strikes me that I might have another requirement
to satisfy: reasonable setup time.  I seem to remember that it took ~5 minutes
to populate the datastructure of all possible games when I was playing around
with this on Monday, and that's not gonna be a fun experience for the user --
waiting 5 minutes before they can start playing tic tac toe.

So, while it wasn't explicitly stated in the reqs, I'm gonna go ahead and 
see about doing that. Meanwhile I'm going to try to be  mindful that scope
creep is bad for a little exercise like this, and if it takes too long to
optimize for time, abandon it.  So first I'll measure current performance and
then I'll make another git branch.

    now = datetime.datetime.now
    b = board.Board()
    b.load('         ')
    root = generate_all_possible.Node(b)
    now(); root.descend(); now()

    >>> datetime.datetime(2014, 6, 11, 10, 33, 29, 741169)
    >>> datetime.datetime(2014, 6, 11, 10, 38, 50, 960624)

Yup, about 5 minutes.

----

Ok, strategy 1 for optimizing load time: generate everything once, store it
in a file, and just load that file on startup.

Experiment 1: cPickle

    print now(); cPickle.dump(root, fp, protocol=-1); print now()

    >>> 2014-06-11 11:16:54.713249
    >>> 2014-06-11 11:17:40.086080

    print now(); foo = cPickle.load(fp); print now()

    >>> 2014-06-11 11:22:53.825928
    >>> 2014-06-11 11:23:29.868691

The loading measurement (36s) is the really important one.  The dumping
measurement (46s) only matters for my development workflow. 
Both seem acceptable, the user interface during play will have to include
a "Please wait approx 30 seconds while the AI loads..." message.
