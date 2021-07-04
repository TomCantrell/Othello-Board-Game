"""
board = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,2,1,0,0,0],
         [0,0,0,1,2,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
"""
"""
board = [ [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,1,2,1,0,0,0],
          [0,0,1,2,2,2,0,0],
          [0,0,1,2,1,0,0,0],
          [0,0,0,2,1,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]
"""
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
def indextostr(t):
    col = ["a","b","c","d","e","f","g","h"]
    return col[t[1]]+str(t[0]+1)
def loadGame():
    ####Need exception to check it is of right form!!!!!!
    
    try:
        with open("game.txt",mode="r",encoding="utf8") as g:
            #if str(file).endswith(".txt")!=True:
                #raise Exception
            dct = dict()
            lst=list()
            for line in g:
                lst.append(line.rstrip("\n"))   #####Might need to explain .rstriphttps://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline-in-python
            tmp=list()
            for _ in range(3,11):
                tmp.append(lst[_])
            bd=list()
            for i in tmp:              ##Turns string into list of lists
                ls=list()             ##Needs changing 
                for _ in i.split(","):
                    ls.append(int(_))
                bd.append(ls)
            dct["player1"]=lst[0]
            dct["player2"]=lst[1]
            dct["who"]=lst[2]
            dct["board"]=bd 
            return dct
    except FileNotFoundError:       ##Not sure on order, does return need to be last?
        print("The file couldn't be found")
def getValidMoves(board,who):
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,-1),(-1,-1),(1,1)]
    lst=list()
    for i in range(8):
        for j in range(8):
            for k in dirs:
                if len(getLine(board,who,(i,j),k))!=0:
                    lst.append((i,j))            
    return list(set(lst))
def strtoIndex(s):
    lst=list(s.strip())
    for _ in s.strip():
        if _==' ':
            lst.remove(_)
    if lst[0].isdigit()==True:
        lst=list(reversed(lst))
    if len(lst)!=2:
        raise ValueError("Not valid")
    col=["a","b","c","d","e","f","g","h"]
    row=[1,2,3,4,5,6,7,8]
    k=0
    c=-1
    for i in col:
        k+=1
        if i==lst[0].lower():
            c=k-1
    if c==-1:
        raise ValueError("Not a Valid move")
    l=0
    for j in row:
        l+=1
        if j==int(lst[1]):
            r=l-1             
    return (r,c)
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
def printBoard(board):
        columns = ["a","b","c","d","e","f","g","h"]
        row = ["+","+","+","+","+","+","+","+","+"]
        print(" "*1,"|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(*columns)," {}-{}-{}-{}-{}-{}-{}-{}-{}".format(*row))
        k=0
        for i in range(len(board)):
            lst=list()
            k += 1
            for j in board[i]:
                if j==0:
                    lst.append(' ')
                if j==1:
                    lst.append('X')
                if j==2:
                    lst.append('O')
            print(k,"|{}|{}|{}|{}|{}|{}|{}|{}|".format(*lst),k)
        print("  {}-{}-{}-{}-{}-{}-{}-{}-{}\n".format(*row)," |{}|{}|{}|{}|{}|{}|{}|{}|".format(*columns))
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
def play():
    ##welcome message
    import time
    print("-"*55)
    print("*"*55)
    print("****"+" "*8+"WELCOME TO TOM'S OTHELLO GAME!"+" "*8+"****")
    print("*"*55)
    print("-"*55, "\n")
    print("Enter the players' names, or type 'C' or 'L'.\n")
    while True:
        player1=input("Name of player 1: ").capitalize()
        if not player1:
            player1=input("Name of player 1: ").capitalize()
        if player1=="L":
            loadGame()###########################################
            player1=loadGame()["player1"]
            player2=loadGame()["player2"]
            who=loadGame()["who"]
            board=loadGame()["board"]
            break
        if player1:
            while True:
                player2=input("Name of player 2: ").capitalize()
                if not player2:
                    player2=input("Name of player 2: ").capitalize()
                if len(player2)!=0:
                    break
            print("Enter q to quit the game.\n Let's play!!!!")
            break
    
    dct=dict()
    dct["player1"]=player1
    dct["player2"]=player2
    dct["who"]=1
    dct["board"] = [[0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,2,1,0,0,0],
                    [0,0,0,1,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0]]
    
    s=0
    k=0 
    printBoard(dct["board"])
    while True:
        d=""
        board=dct["board"]
        if s%2==0:
            who=1
            d=dct["player1"]
            print(dct["player1"],"'s move")
        else:
            who=2
            d=dct["player2"]
            print(dct["player2"],"'s move")
        #print(dct["board"])#########
        lst=getValidMoves(board, who)
        #print("who=",who)
        """
        for i in lst:
            print("Valid moves are\n", indextostr(i))
        """   
        if len(lst)==0:
            if k==2:
                print("--------------"+" "*8+"Game Finished!"+" "*8+"---------------\n")
                break
            k+=1
            print("No Valid Moves for", d, ", skipping player.")
            s+=1
        if d=="C":
            print("Computer is thinking...")
            time.sleep(3)
            move=indextostr(suggestMove1(board,who))
            print("The Computer chose ",indextostr(suggestMove1(board,who)))
        else:
            move=str(input("Please enter a move: "))#### Tom (X), C (O)
            #print(strtoIndex(move))
            if move=="q":
                print("--------------"+" "*8+"Game Stopped"+" "*8+"---------------\n")
                break
        try:
            if strtoIndex(move) not in lst:
                print("Not a valid Move\n")
                printBoard(dct["board"])
            if strtoIndex(move) in lst:
                for i in getValidMoves(board,who):
                    if i==strtoIndex(move):
                        dct["board"]=makeMove(board, strtoIndex(move), who)
                        printBoard(dct["board"])
                        s+=1
                        #print(board)
        except ValueError:
            print("Not a valid move\n")
            printBoard(dct["board"])
            pass
        #print(s)
        
        if scoreBoard(board)>0:
            print("Advantage", dct["player1"], "(X)")
        if scoreBoard(board)<0:
            print("Advantage", dct["player2"], "(O)")
        if scoreBoard(board)==0:
            print("No Advantage")
    
    p1score=0
    p2score=0
    for i in board:
        for j in i:
            if i==1:
                p1score+=1
            if i==2:
                p2score+=1
    if scoreBoard(board)>0:
        print(dct["player1"], " wins! With a score of ", p1score)
    if scoreBoard(board)<0:
        print(dct["player2"], " wins! With a score of ", p2score)
    if scoreBoard(board)==0:
        print("No winner")














