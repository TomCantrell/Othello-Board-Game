"""
Score the board
"""
def scoreBoard(board):
    p1score=0
    p2score=0
    for i in board:
        for j in i:
            if j==1:
                p1score+=1
            if j==2:
                p2score+=1
    return p1score-p2score

board = [ [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,1,2,1,0,0,0],
          [0,0,1,2,2,2,0,0],
          [0,0,1,2,1,0,0,0],
          [0,0,0,2,1,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]
print(scoreBoard(board))
