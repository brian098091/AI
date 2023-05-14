import time
from copy import deepcopy
start_time = time.time()
board_org = []
with open('input.txt','r') as f:
    row, col = [int(x) for x in next(f).split()]
    board_org = [[int(x) for x in line.split()] for line in f]
board = deepcopy(board_org)
MAX, MIN = 1000, -1000
#檢查是否結束
def check_finish(board):
    for i in range(row):
            for j in range(col):
                if board[i][j] != 0:
                    return False
    return True
# alpha-beta pruning
def abp(board,Player,score0, alpha, beta):
    global ROW,m,board_org 
    if check_finish(board) == True :
        return score0
    board0 = deepcopy(board)
    score = deepcopy(score0)
#檢查為min 或 max node
    if Player == True :
        best = MIN
# 從row 1到row n
        for i in range(row):
            check_0 = True
# 若beta <= alpha pruning
            if beta <= alpha:
                continue
            for j in range(col):
                if board0[i][j] == 1 :
                    check_0 = False
                    score = score + 1
                    board0[i][j] = 0
# 若還沒結束繼續往下一層找
            if check_0 == False:
                val = abp(board0,False,score,alpha,beta)
# 檢查是否更新value
                if best < val :
                    best = val
                    if board == board_org :
                        ROW = True
                        m = i+1
                alpha = max(alpha, best)
                board0 = deepcopy(board)
                score = deepcopy(score0)
# 從col 1到col m
        for i in range(col):
            check_0 = True
            if beta <= alpha:
                continue
            for j in range(row):
                if board0[j][i] == 1 :
                    check_0 = False
                    score = score + 1
                    board0[j][i] = 0
            if check_0 == False:
                val = abp(board0,False,score,alpha,beta)
                if best < val :
                    best = val
                    if board == board_org :
                        ROW = False
                        m = i+1
                alpha = max(alpha, best)
                board0 = deepcopy(board)
                score = deepcopy(score0)
        return best
    else :
        best = MAX
        for i in range(row):
            check_0 = True
            if beta <= alpha:
                continue
            for j in range(col):
                if board0[i][j] == 1 :
                    check_0 = False
                    score = score - 1
                    board0[i][j] = 0
            
            if check_0 == False:
                val = abp(board0,True,score,alpha,beta)
                if best > val :
                    best = val
                    if board == board_org :
                        ROW = True
                        m = i+1
                beta = min(beta, best)
                board0 = deepcopy(board)
                score = deepcopy(score0)
        for i in range(col):
            check_0 = True
            if beta <= alpha:
                continue
            for j in range(row):
                if board0[j][i] == 1 :
                    check_0 = False
                    score = score - 1
                    board0[j][i] = 0
            if check_0 == False:
                val = abp(board0,True,score,alpha,beta)
                if best > val :
                    best = val
                    if board == board_org :
                        ROW = False
                        m = i+1
                beta = min(beta, best)
                board0 = deepcopy(board)
                score = deepcopy(score0)
        return best
# 劃出棋盤
def print_board(board):
    for i in range(row):
        for j in range(col):
            print(board[i][j], end=' ')
        print()
        
def play(board,com) :
    while check_finish(board) == False :
        print("board:")
        print_board(board)
        rc,x = input("Player1's Trun:").split()
        board = change(board,rc,x,1)
        print("board:")
        print_board(board)
        if com == True :
            abp(board,True,0,MIN,MAX)
            if ROW == True :
                print("Computer's Trun:","row",m)
                board = change(board,"row",m,2) 
            else :
                print("Computer's Trun:","col",m)
                board = change(board,"col",m,2)
        else :  
            rc,x = input("Player2's Trun:").split()
            board = change(board,rc,x,2)
    print("board:")
    print_board(board)

def change(board,rc,x,player) :
    x = int(x) - 1
    if rc == "row" :
        for i in range (col) :
            if board[x][i] != 0 :
                score(player)
                board[x][i] = 0
    elif rc == "col" :
        for i in range (row) :
            if board[i][x] != 0 :
                score(player)
                board[i][x] = 0
    else :
        print("invalid move!")
    return board

def score(player) :
    global score1,score2
    if player == 1 :
        score1 = score1 + 1
    else :
        score2 = score2 + 1

def main() :
    points = abp(board,True,0,MIN,MAX)
    if ROW :
        lines0 = ["Row # : ",str(m)]
    else :
        lines0 = ["Colums # : ",str(m)]
    lines=["\n",str(points)," points\n","Total rum time = ",str(time.time() - start_time)," second\n",]
    fp = open("output.txt","w")
    fp.writelines(lines0  + lines)

def winner(com) :
    if(com == True) :
        if score1 > score2 :
            print(" Player Win!!")
        elif score1 == score2 :
            print(" Tie!!")
        else :
            print(" Computer Win!!")
    else :
        if score1 > score2 :
            print(" Player1 Win!!")
        elif score1 == score2 :
            print("Tie!!")
        else :
            print(" Player2 Win!!")


if __name__ == "__main__":
    main()
    yn = input("Do you want to play with this board(y/n):")
    if yn == "n" :
        exit()
    score1 = 0
    score2 = 0
    player = input("Please enter the number of player(1 or 2):")
    if player == "1" :
        computer = True
    else :
        computer = False
    play(board_org,computer)
    print("Result : ")
    if computer == True :
        print(" Player's score : ",score1,"\n","Computer's score : ",score2)
    else :
        print(" Player1's score : ",score1,"\n","Player2's score : ",score2)
    winner(computer)

exit()
    

