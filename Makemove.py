"""
Make a move
"""
def getLine(board,who,pos,dir):
    lst=list()
    i=pos[0]
    j=pos[1]
    if board[i][j]!=0:
        return lst
    while True:
        if i+dir[0]==8 or j+dir[1]==8:######need to deal with these better
            lst=list()
            break
        if i+dir[0]==-1 or j+dir[1]==-1:
            lst=list()
            break
        if board[i+dir[0]][j+dir[1]]==0:
            lst=list()
            break
        if board[i+dir[0]][j+dir[1]]==who:
            break
        lst.append((i+dir[0],j+dir[1]))
        i+=dir[0]
        j+=dir[1]
    return lst
def makeMove(board,move,who):
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,-1),(-1,-1),(1,1)]
    lst=list()
    for i in dirs:
        if len(getLine(board,who,move,i))!=0:
            for j in getLine(board, who, move, i):
                lst.append(j)
            lst.append(move)
            print(lst)
    for k in lst:
        board[k[0]][k[1]]=who
    return board

##Testing

board = [ [0,0,0,0,0,0,0,0],
          [0,0,1,2,0,0,0,0],
          [0,0,0,1,2,2,2,0],
          [0,0,0,2,2,2,2,2],
          [0,0,0,2,2,1,0,0],
          [0,0,1,2,0,1,0,0],
          [0,0,0,0,2,1,0,0],
          [0,0,0,0,0,0,0,0]]

#print(printBoard(board))
#print(makeMove(board,(3,1),2))

