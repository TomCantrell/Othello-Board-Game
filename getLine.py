"""
Line of opponents pieces
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



"""
############Testing
"""
board = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,1],
         [0,0,0,0,1,2,2,0],
         [0,0,0,1,1,2,0,0],
         [0,0,0,2,2,2,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
"""
print(getLine(board,1,(6,3),(-1,1)))   
print(getLine(board,2,(4,2),(0,1)))    
print(getLine(board,2,(3,3),(1,1)))
print(getLine(board,1,(6,6),(-1,-1)))
print(getLine(board,1,(4,6),(0,-1)))
print(getLine(board,1,(6,4),(-1,0)))
print(getLine(board,2,(2,5),(1,0)))
print(getLine(board,1,(2,6),(1,-1)))
print(getLine(board,1,(2,5),(1,0)))
print(getLine(board,1,(6,6),(0,-1)))
"""
    