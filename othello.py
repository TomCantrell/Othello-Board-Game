"""
A Python module for the othello game.

This module comprises of many functions which all contribute to the final main
function play() which deals with the actual game flow. 


Full name: Thomas Cantrell
StudentId: 10170539
Email:thomas.cantrell@student.manchester.ac.uk
"""
def newGame(player1,player2):
    """
    This function takes the names of players 1 and 2, then it returns a 
    dictionary containing a variable who (initialsed as who=1) and a list of 
    lists which is the initialised board variable. 
    """
    game = dict()
    game["player1"] = str(player1) #Black player
    game["player2"] = str(player2) #White player
    game["who"] = 1
    game["board"] = [ [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,2,1,0,0,0],
                      [0,0,0,1,2,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0]]
    # TODO: Initialize dictionary for a new game
    return game 
#########################################################################        
# TODO: All the other functions of Tasks 2-12 go here.
# USE EXACTLY THE PROVIDED FUNCTION NAMES AND VARIABLES!
def printBoard(board):
    """
    This function takes a list of lists and prints out a nicely formatted 
    board. Columns are labelled at the top of the board and the bottom of board
    with a through h, rows are labelled either side of the board with 1 through
    8.
    
    Two lists of strings are initialised, columns and row with columns 
    labelling the columns and row used for making the edge of the board clear.
    A variable k is then initialised and a for loop goes through each list in 
    board initialising an empty list lst each time. If the elements in the list
    are non-zero (1 or 2), the if statements then add an X or O accordingly, if
    an element is zero then an empty string is simply added.
    
    This is then printed with vertical bars in between X's, O's and empty 
    strings. Furthermore at the bottom of the board the letters are added to
    denote the columns again much like before at the top of the board.
    
    """
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
def strtoIndex(s):
    """
    This function takes a string s and then returns an index in the form of a 
    tuple. This tuple refers to the position in the list of lists in the board
    variable. The first few lines aim to deal with the various versions of a
    string a user can input i.e " 4 c" returns the same thing as "c4".
    
    Firstly a list called lst is created by taking a list of s.strip(), where 
    s.strip() strips the spaces (if there are any) from the beginning and end of
    the string. Then the for loop removes and spaces in between so that there 
    is only characters left in the list and no spaces. The if statement then 
    checks if the first element in the list is a digit (to check whether the 
    user has entered "4c" or "c4" and deal with each of them accordingly), this
    is done with the function .isdigit(). If it is a digit then the list is 
    reversed using the reverse function.
    
    Then two lists are initialised col and row, which refer to the columns and
    rows respectively. Furthermore k is initialsed at 0 and c at -1.
    
    Then a for loop, which loops over col checks if any of the elements in col 
    are equal to the lower case zero-th element in lst also while the variable 
    k is increasing each loop. lst[0].lower is used because the user may have
    entered "C4" instead of "c4", hence it means the user can enter a move 
    in upper/lowercase. Then the variable c=k-1 gives the indice of the 
    associated column position (takes a value in 0,..,7). 
    However if c==-1 after the for loop has covered all elements in col, then a
    valueError is raised as this means the move that has been entered must not 
    be valid.
    
    The variable l is then initialised as l=0, then a for loop over row checks 
    if any of the elements are equal to the 2nd element in lst (lst[1]). It 
    makes sense to take int(lst[1]) as we know this will a number otherwise a 
    valueError would've been raised. Similarly as with the other for loop r=l-1
    gives the associated board row position.
    
    """
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
    r=-1
    l=0
    for j in row:
        l+=1
        if j==int(lst[1]):
            r=l-1 
    if r==-1:
        raise ValueError("Not a Valid move")
    return (r,c)
def indextostr(t):
    """
    This function takes a tuple and then returns a string, which refers to a
    board position on the printed board. 
    A list col is initialised which refers to the columns of the printed board.
    The function returns a string made up of col[t[1]] (t[1] refers to the 
    second position in the tuple) and the row is made up from t[0] then add 1.
    """
    col = ["a","b","c","d","e","f","g","h"]
    return col[t[1]]+str(t[0]+1)
def loadGame():
    """
    This function takes no arguments, and attempts to load a dictionary from a 
    .txt file. It then returns a dictionary with player1 and player2 assigned 
    to the first two lines of the text file. The variable who is then set equal
    to the third line, and the variable board is set equal to lines 3 through
    11. 
    
    Firstly the function initialises an empty dictionary called dct along with
    a list lst. Then the function attempts to open a file called game.txt and
    this assigned as g, it is being opened for reading. Then this file is read 
    line by line and since the file is in a particular format, the names of the
    players, who and the board can all be obtained by simply setting the lines 
    of this file equal to them. For example the board variable takes lines 3 to
    11, and similarly the first 2 lines will be the players names. 
    
    If the file cannot be opened because it cannot find a text file called 
    game.txt then an exception for FileNotFoundError prints "The file couldn't
    be found".
    
    After this three if statements check that the first two lines are indeed 
    string, if the board is the right type and if who is equal to an integer.
    Hence the format of the text file has been checked, if it is not of the 
    correct form a ValueError is raised.
    
    The function returns the dictionary dct, with player1 and player2's 
    names assigned along with the board and who.
    """   
    try:
        with open("game.txt",mode="r",encoding="utf8") as g:
            dct = dict()
            lst=list()
            for line in g:
                lst.append(line.rstrip(" \n"))   #.rstriphttps://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline-in-python
            tmp=list()
            for _ in range(3,11):
                tmp.append(lst[_])
            bd=list()
            for i in tmp:              
                ls=list()             
                for _ in i.split(","):
                    ls.append(int(_))
                bd.append(ls)
            dct["player1"]=lst[0]
            dct["player2"]=lst[1]
            dct["who"]=int(lst[2])
            dct["board"]=bd 
            if type("player1") and type(dct["player2"]) != str:
                raise ValueError
            if type(dct["board"])!=list:
                raise ValueError
            if type(dct["who"]) != int:
                raise ValueError
            return dct
    except FileNotFoundError:       
        print("The file couldn't be found \n")
    except ValueError:
        print("File not of correct format \n")
def getLine(board,who,pos,dir):
    """
    This function takes 4 input arguments namely board, who, pos (position) and
    dir (direction) and it then returns a list of oppents pieces which form a
    line. This function initialises an empty list then checks the next position
    in the direction given and then checks that it is not equal to zero i.e if 
    that particular position is already occupied by a players piece. Then it 
    checks which player occupies this piece, if it is the same as the variable 
    who, it then stops and doesn't check the rest of line as this wouldn't be
    a valid move.
    However if the next piece in the given direction is indeed the opponents
    piece, the position will be added to the empty list and move on to the 
    next piece in the given direction. It will continue to do so until it
    reaches a position occupied by the value who or zero. If the line of 
    opponents pieces ends in a zero, the list lst is set empty and thus an
    empty list is returned. 
    Otherwise the line of opponents pieces ends in the value of who i.e the
    value of who for the current player. Thus a line of opponents pieces is 
    obtained and the list of positions of these pieces is returned.
    """
    lst=list()
    i=pos[0]
    j=pos[1]
    if board[i][j]!=0:
        return lst
    while True:
        if i+dir[0]==8 or j+dir[1]==8:#
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
def getValidMoves(board,who):
    """
    This function takes 2 input arguments namely the variable board and the 
    variable who. 
    This function goes through each board position and at each position it goes
    through a list of directions making use of the getLine function above. If 
    the list which the getLine function returns is non empty i.e there are
    valid moves with line(s) of opponents pieces to be obtained. Then the
    position, at which the getLine function is being tested, is added to a list
    lst. 
    This function then returns a list of positions on the board where the
    player who could potentially go. 
    """
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,-1),(-1,-1),(1,1)]
    lst=list()
    for i in range(8):
        for j in range(8):
            for k in dirs:
                if len(getLine(board,who,(i,j),k))!=0:
                    lst.append((i,j))            
    return list(set(lst))

def makeMove(board,move,who):
    """
    This function takes 3 input arguments namely board, move (a tuple 
    refering to a board position) and the variable who.
    A list of directions is first initialsed, along with an empty list. A for 
    loop then goes through all the directions and checks if getLine function 
    produces a non empty list with each direction. If the list is indeed non
    empty, then a for loop goes through the list of opponents pieces (list of
    tuples from getLine) and then adds it to lst along with the position "move"
    the player wishes to make.
    If the list lst is non empty, a for loop then adds it to the board changing
    the positions to the value of the variable who. An updated board is then
    returned.
    """
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

def scoreBoard(board):
    """
    This function takes 1 input argument board and returns an integer. 
    Two variables are initialsed p1score and p2score, these refer to player1's
    score and player2's score respectively. Then two for loops go through the 
    board positions and add to the initalised p1score and p2score if a position
    is occupied by a 1 or 2. 
    The function then returns p1score-p2score, so if scoreBoard is positive 
    there are more 1's than 2's (giving an adventage to player1), and if 
    scoreBoard is negative then there are more 2's than 1's (giving an 
    advantage to player2). If scoreBoard is equal to zero then there is no
    advantage to either player.
    """
    p1score=0
    p2score=0
    for i in board:
        for j in i:
            if j==1:
                p1score+=1
            if j==2:
                p2score+=1
    return p1score-p2score

def suggestMove1(board,who):
    """
    This function takes 2 input arguments board and who. Two lists are 
    initialised and lst is set equal to getValidMoves(board,who), this is so 
    that getValidMoves function is only called once, so it is more efficient.
    The modules copy and random are imported at the beginning of the function.
    Then a for loop goes through the valid moves of the player who, the 
    board2 variable is assigned to a deepcopy of the original board. In each 
    loop makeMove(board2,i,who) (where i represents a valid move) is evaluated
    and then the scoreBoard function evaluates the returned board from 
    makeMove. This score is then added to the initialised empty list t, thus 
    creating a list of scores from potential moves a player could make.
    
    Then there are two if statements where one finds the maximum scoreBoard
    value and then adds the position(s) at which this maximum scoreBoard value 
    occurs to the list l (which was initialised at the beginning). The other if
    statement finds the minimum scoreBoard value and adds the position(s) where
    this occurs to the list l. If there are no valid moves available then None
    is returned.
    
    After the list l is created, random.choice(l) chooses at random a move
    which achieves the largest score to the advantage of player who.
    Random.choice is used because there may be more than one board position 
    which achieves max/minimum score. Hence the function returns a tuple 
    chosen at random from the list l. 
    """
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

##########################################################################
# ------------------- Main function --------------------
def play():
    """
    This function is the main part of the module and takes care of the overall
    operation of the game. This function takes no input arguments.
    
    Firstly the module time is imported, then a welcome message is displayed
    to the user, along with another message on what to input if the user wishes
    to load a game or play the computer. A while loop is then used for asking
    the user(s) names and the while loop means that the names of either player
    can be repeatedly asked for if the user is entering empty strings, also c 
    can be typed in as either player 1 or 2. Furthermore the use of 
    .capitalize() means that the name of player 1 and 2 are capitalised.
    
    Then a dictionary is initialised called dct, this is set equal to the 
    dictionary returned from the function newGame(player1,player2) as this 
    initialises the starting board and sets who equal to 1. If l is typed in as
    player1 then the function loadGame() opens a game from a text file and 
    uses the names and board from that to jump straight into a game, this is
    done by setting loadGame() equal to dct.     
    """
    ##welcome message
    import time
    print("-"*55)
    print("*"*55)
    print("****"+" "*8+"WELCOME TO TOM'S OTHELLO GAME!"+" "*8+"****")
    print("*"*55)
    print("-"*55, "\n")
    print("Enter the players' names, or type 'C' to play the computer or 'L' to load a game.\n")
    while True:
        dct=dict()
        player1=input("Name of player 1: ").capitalize()
        if not player1:
            player1=input("Name of player 1: ").capitalize()
        if player1=="L":
            if loadGame() is None:
                player1=""
                print("Please enter a player name or attempt to load the game again")
            else:
                print("Entering loaded game. \n")
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
    """
    After the dictionary has been set, the game begins and the user can enter q
    when it is their move to quit the game. The first player is always (X) and
    the second (O) and this is shown to the user(s) at the beginning. Two 
    variables s and k are initialised at zero, then printBoard() prints the 
    starting board (it would print the board from the text file if l was 
    inputted as player 1).
    
    Inside the while loop another variable d is initialised as an empty string.
    Then an if and else statement checks whether s is even or odd and this 
    determines the variable who and ensures that it alternates players each
    turn. The variable d is also set to the name of player1 or player2 
    depending on whether s is odd/even. 
    
    Another variable lst is set to getValidMoves(board, who), thus obtaining a 
    list of the valid moves of that particular player. If lst is empty then 
    k increases by 1 and the user is informed that there are no valid moves for
    that particular player, s is also increased by 1 thus moving it on to the 
    next players turn. The variable k is set back to zero if the next player 
    can go, otherwise k will increase to 2 and thus the game will be finished
    and the break statement breaks out of the while loop. 
    
    Next, if lst is non-empty then it checks the name of the player and sees if
    it is the computers turn. If it is indeed the computers turn "Computer is 
    thinking..." is printed and time.sleep(2) represents the thinking time. 
    A new variable move is then set equal to suggestMove1(board,who). Otherwise
    it'll be the users turn, so the user is asked to input a move, this is then
    turned into a string. Here it is also checked if the move is equal to "q" 
    which would quit the game with the break statement. 
    
    Then it attempts to check whether or not its a valid move via the 
    strtoIndex function. If its not a valid move or if strtoIndex raises an 
    error, it raises an error and informs the user that it is not a valid move.
    Otherwise it is a valid move and this move is then made via the makeMove
    function and the new board is set to dct["board"], this is then displayed
    to the user, k is then set to zero as a move has been made and s has 
    increased so that in the next loop it is the other players turn. 
    
    If the scoreBoard function returns a positive value for this new board then
    player1 has the advantage so this is displayed to the user(s), a similar 
    thing is done if scoreBoard is negative. If scoreBoard returns zero then
    there is no advantage and so "No advantage is printed".
    
    Outside of this while loop the scores are added up and the winner is 
    decided, this is then displayed to the user(s).     
    """
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
        lst=getValidMoves(board, who)
        if len(lst)==0:
            k+=1
            print("No Valid Moves for", d, ", skipping player. \n")
            s+=1
        if k==2:
            print("--------------"+" "*8+"Game Finished!"+" "*8+"---------------\n")
            break
        if len(lst)!=0:    
            if d=="C":
                print("Computer is thinking...")
                time.sleep(2)
                move=indextostr(suggestMove1(board,who))
                print("The Computer chose ",indextostr(suggestMove1(board,who)))
            else:
                move=str(input("Please enter a move: "))#### Tom (X), C (O)
                if move=="q":
                    print("--------------"+" "*8+"Game Stopped"+" "*8+"---------------\n")
                    break
        try:
            if strtoIndex(move) not in lst:
                raise IndexError
            if strtoIndex(move) in lst:
                for i in getValidMoves(board,who):
                    if i==strtoIndex(move):
                        dct["board"]=makeMove(board, strtoIndex(move), who)
                        printBoard(dct["board"])
                        k=0
                        s+=1
        except IndexError:
            print("Not a valid move\n")
            printBoard(dct["board"])
        except ValueError:
            print("Not a valid move\n")
            pass
            printBoard(dct["board"])
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
# the following allows your module to be run as a program
if __name__ == '__main__' or __name__ == 'builtins':
    play()
    
    