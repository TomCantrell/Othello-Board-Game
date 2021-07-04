"""
Play the game
"""
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
        dct=dict()
        player1=input("Name of player 1: ").capitalize()
        if not player1:
            player1=input("Name of player 1: ").capitalize()
        if player1=="L":
            dct=loadGame()
            break
        if player1:
            while True:
                player2=input("Name of player 2: ").capitalize()
                if not player2:
                    player2=input("Name of player 2: ").capitalize()
                if len(player2)!=0:
                    dct = newGame(player1,player2)
                    break
            print("Enter q to quit the game.\n Let's play!!!!")
            break    
    #print(dct["player1"],dct["player2"])
    #dct["board"]=board
    print(dct["player1"],"= X",8*" ",dct["player2"],"= O")
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
        if len(lst)==0:
            k+=1
            print("No Valid Moves for", d, ", skipping player.")
            s+=1
        if k==3:
            print("--------------"+" "*8+"Game Finished!"+" "*8+"---------------\n")
            break
        if len(lst)!=0:    
            if d=="C":
                print("Computer is thinking...")
                time.sleep(1)
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
            if j==1:
                p1score+=1
            if j==2:
                p2score+=1
    if scoreBoard(board)>0:
        print(dct["player1"], "(X) wins! With a score of", p1score)
        print(dct["player2"], "(O) scores", p2score)
    if scoreBoard(board)<0:
        print(dct["player2"], "(O) wins! With a score of", p2score)
        print(dct["player1"], "(X) scores", p1score)
    if scoreBoard(board)==0:
        print("No winner")
        