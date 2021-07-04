"""
Initilize a new game
"""
game = {
     'player1' : 'Tom',
     'player2' : 'C',
     'who' : 1,
     'board' : [ [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,2,1,0,0,0],
                 [0,0,0,1,2,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0]]
                    }
def newGame(player1 ,player2):
    game["player1"] = str(player1) #Black player
    game["player2"] = str(player2) #White player
    game["who"] = 1
    return game
   