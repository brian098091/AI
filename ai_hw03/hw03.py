import time
from copy import deepcopy
start_time = time.time()
board_org = []
with open('input.txt','r') as f:
    row, col = [int(x) for x in next(f).split()]
    board_org = [[int(x) for x in line.split()] for line in f]
board = deepcopy(board_org)
MAX, MIN = 1000, -1000

def check_finish(board):
    for i in range(row):
            for j in range(col):
                if board[i][j] != 0:
                    return False
    return True
def abp(board,Player,score0, alpha, beta):
    global ROW,m,board_org 
    if check_finish(board) == True :
        return score0
    board0 = deepcopy(board)
    score = deepcopy(score0)
    if Player == True :
        best = MIN
        for i in range(row):
            check_0 = True
            if beta <= alpha:
                continue
            for j in range(col):
                if board0[i][j] == 1 :
                    check_0 = False
                    score = score + 1
                    board0[i][j] = 0
            if check_0 == False:
                # print(board0,score)
                val = abp(board0,False,score,alpha,beta)
                if best < val :
                    best = val
                    if board == board_org :
                        ROW = True
                        m = i+1
                alpha = max(alpha, best)
                board0 = deepcopy(board)
                score = deepcopy(score0)
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
                # print(board0,score)
                val = abp(board0,False,score,alpha,beta)
                if best < val :
                    best = val
                    if board == board_org :
                        ROW = False
                        m = i+1
                alpha = max(alpha, best)
                board0 = deepcopy(board)
                score = deepcopy(score0)
        # print(ROW,m)
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
                # print(board0,score)
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
                # print(board0,score)
                val = abp(board0,True,score,alpha,beta)
                if best > val :
                    best = val
                    if board == board_org :
                        ROW = False
                        m = i+1
                beta = min(beta, best)
                board0 = deepcopy(board)
                score = deepcopy(score0)
        # print(ROW,m)
        return best

points = abp(board,True,0,MIN,MAX)
if ROW :
    lines0 = ["Row # : ",str(m)]
else :
    lines0 = ["Colums # : ",str(m)]
lines=["\n",str(points)," points\n","Total rum time = ",str(time.time() - start_time)," second\n",]
fp = open("output.txt","w")
fp.writelines(lines0  + lines)
exit()
    

