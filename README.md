# Othello-Board-Game

The code shared here enables the user to play an interactive board game in the python console. The board game played by this python module is Othello or Reversi. The classic board game of Othello/Reversi is played on an unchecked 8x8 board where four pieces (two from each player arranged diagonally) at the centre of the board gives the starting position of the game. In this version which is performed through interactions in the python console, a combination of numbers 1-8 and A-H are used to define positions on the board. 

In the code listed here, the functions which can carry out moves inputted by the player(s) are shown. Along with these functions there are also functions that allow for a variety of inputs from the player(s) to be understood by the game (for example "4g" and "  G4  " are understood analogously). A function that is able to calculate all the valid moves for the player(s) is also used so that no invalid moves can be played. Furthermore the game automatically keeps the score and returns the current scores to the player(s) at the end of each turn as well as who is winning/losing at any point in the game. The game can be played by copying and pasting the .py file Othello_{ThomasCantrell} into an empty .py file and running it. 

The game begins with a welcome message and requests the user(s) to type their names into the python module. If one wishes to play the computer, one must type "c" in repsonse to one of the player names (typing "c" twice as the player names means the computer will play itself). The computer that one plays if one types "c" into the console is a naive AI that plays the valid move that increases their scores the most at that stage. If there is more than one valid move that increases the score of the computer by the same maximum amount, then a move is chosen randomly from these possible (maximum scoring) moves. The corner pieces are particularly powerful in Othello in that they cannot be altered once secured by any of the players, hence to improve this naive AI (which can see no further than its current move on the board) one could introduce a bias so that the AI plays more aggresive to attain these corner pieces.     

                               -----   Copy and paste the code from othello.py and enjoy!   -----




