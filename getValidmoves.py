"""
Get a list of all the valid moves
"""
def getLine(board,who,pos,dir):
    lst=list()
    i=pos[0]
    j=pos[1]
    if board[i][j]!=0:
        return lst
    while True:
        if i+dir[0]==8 or j+dir[1]==8:        ######need to deal with these better
            break
        if i+dir[0]==-1 or j+dir[1]==-1:
            break
        if board[i+dir[0]][j+dir[1]]==0:
            lst=list()
            #print("You can't do that m8")
            break
        if board[i+dir[0]][j+dir[1]]==who:
            break
        lst.append((i+dir[0],j+dir[1]))
        i+=dir[0]
        j+=dir[1]
    return lst
def getValidMoves(board,who):
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,-1),(-1,-1),(1,1)]
    lst=list()
    for i in range(8):
        for j in range(8):
            for k in dirs:
                if len(getLine(board,who,(i,j),k))!=0:
                    lst.append((i,j))            
    return list(set(lst))

###testing

board = [ [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,1,2,1,0,0,0],
          [0,0,1,2,2,2,0,0],
          [0,0,1,2,1,0,0,0],
          [0,0,0,2,1,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]
print(getValidMoves(board,2))
[(6, 4), (1, 3), (5, 5), (4, 5),(3, 1), (2, 1),(1, 4), (1, 5), (5, 1), (2, 5),
 (4, 1), (1, 1), (6, 5)]
print(getValidMoves(board,1))
[(6, 4), (2, 6), (4, 6), (1, 4), (6, 2), (3, 6), (5, 2)]
