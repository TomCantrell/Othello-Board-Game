"""
Print a nicely formatted board
"""
board = [ [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,2,1,0,0,0],
          [0,0,0,1,2,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]
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
    

"""

columns = ["a","b","c","d","e","f","g","h"]
row = ["+","+","+","+","+","+","+","+","+"]
print("  |{}|{}|{}|{}|{}|{}|{}|{}|\n".format(*columns)," {}-{}-{}-{}-{}-{}-{}-{}-{}".format(*row))
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
 


def printboard(board):
    columns = ["a","b","c","d","e","f","g","h"]
    row = ["+","+","+","+","+","+","+","+","+"]
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
    pboard =  
"""


    