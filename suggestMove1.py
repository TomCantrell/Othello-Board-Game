"""
An easy computer opponent
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
def makeMove(board,move,who):
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,-1),(-1,-1),(1,1)]
    lst=list()
    for i in dirs:
        if len(getLine(board,who,move,i))!=0:
            for j in getLine(board, who, move, i):
                lst.append(j)
            lst.append(move)
    for k in lst:
        board[k[0]][k[1]]=who
    return board

def suggestMove1(board,who):
    lst=getValidMoves(board,who)
    t=list()
    l=list()
    import copy
    import random
    for i in lst:
        board2=copy.deepcopy(board)
        t.append(scoreBoard(makeMove(board2,i,who)))
    if who==1:
        for j in range(len(t)):
            if t[j]==max(t):
                l.append(lst[j])
    if who==2:
        for j in range(len(t)):
            if t[j]==min(t):
                l.append(lst[j])
    if len(l)==0:
        return None
    return random.choice(l)

############TEST
"""
#print(suggestMove1(board,2))
#print(suggestMove1(board,1))

for i in getValidMoves(board,2):
    board2=copy.deepcopy(board)
    print(printBoard(board2))
    print(i)
    print(makeMove(board2, i, 2))
    print(printBoard(makeMove(board2,i,2)))
    print(scoreBoard(makeMove(board2,i,2)))
    print(t)
    print(lst)
    print(l)
"""    








