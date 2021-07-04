"""
Load a game from a file
"""
def loadGame():
    ####Need exception to check it is of right form!!!!!!
    
    try:
        with open("game.txt",mode="r",encoding="utf8") as g:
            #if str(file).endswith(".txt")!=True:
                #raise Exception
            dct = dict()
            lst=list()
            for line in g:
                lst.append(line.rstrip(" \n"))   #####Might need to explain .rstriphttps://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline-in-python
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
        
        
        ["0,0,0,0,0,0,0,0","0,0,0,0,0,0,0,0","0,0,1,2,1,0,0,0","0,0,1,2,2,2,0,0","0,0,1,2,1,0,0,0",
"0,0,0,2,1,0,0,0","0,0,0,0,0,0,0,0","0,0,0,0,0,0,0,0"]