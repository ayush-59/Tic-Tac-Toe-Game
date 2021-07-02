import random
board=[" " for i in range(10)]

def interface():
    print("******WELCOME******")
    print("****TIC TAC TOE****")
    print("ENTER CHOICE FROM 1 TO 9")

def boarddes():
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[1],board[2],board[3]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[4],board[5],board[6]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[7],board[8],board[9]))
    print("   |   |   ")
    print("           ")

def isWinner(x):
    if(board[1]==x and board[2]==x and board[3]==x or
    board[4]==x and board[5]==x and board[6]==x or
    board[7]==x and board[8]==x and board[9]==x or
    board[1]==x and board[5]==x and board[9]==x or
    board[3]==x and board[5]==x and board[7]==x or
    board[1]==x and board[4]==x and board[7]==x or
    board[3]==x and board[6]==x and board[9]==x or
    board[2]==x and board[5]==x and board[8]==x ):
        return True
    
def is_draw():
    possibleMoves=[x for x,letter in enumerate(board) if letter==" " and x!=0]
    return len(possibleMoves) > 0


def compTurn():
    possibleMoves=[x for x in range(1,10) if board[x]==" "]
    for x in ['O','X']:
        for let in possibleMoves:
            board[let]=x
            if isWinner(x):
                return let
            board[let]=" "

    choices=[]
    corners=[1,3,7,9]
    for x in corners:
        if x in possibleMoves:
            choices.append(x)
    if len(choices)>0:
        x=random.choice(choices)
        return x

    if 5 in possibleMoves:
        return 5

    edges=[2,4,6,8]
    for x in edges:
        if x in possibleMoves:
            choices.append(x)
    if len(choices)>0:
        x=random.choice(choices)
        return x


def getInput():
    possibleMoves=[x for x,letter in enumerate(board) if letter==" " and x!=0]
    n=0
    while n not in possibleMoves:
        n=int(input("YOUR TURN "))
        if n not in possibleMoves:
            print("invalid input")
    board[n]='x'

def isboardFull():
    if(board.count(' ')>1):
        return False
    boarddes()
    print("GAME TIE! WELL PLAYED")
    return True

interface()
while(1):
    getInput()
    boarddes()
    if(isWinner('x')):
        print("YOW WIN")
        break;
    if(isboardFull()):
        break;
    compTurn()
    boarddes()
    if(isWinner('o')):
        print("YOU LOSE")
        break;
