import numpy as np
from copy import deepcopy
import time
start_time = time.time()
with open('input.txt', 'r') as fh:
    input = fh.read()
list_or = list(map(int,input.split(' ')))
n = len(list_or)
print(list_or)
list = []
check = []
ans = []
move = 0
repeat = []
tmp = []
finish = False
check_fin = 0
check_same = 0
repeat_time = 0
no_solution = True
limit = 0 
layer = 1
def ids(list_org,n):
    global move,finish,repeat_time,check_fin,repeat,tmp,check_same,limit,layer,no_solution
    # print(list_org,"rea:",repeat,"layer",layer)
    
    if finish == True :
            return
#從1按到n+1，為零就跳過
    for x in range(1,n+1) :
        list = deepcopy(list_org)
        if list[x-1] != 0 :
            no_solution = False
            check.clear() 
            move = move + 1
            ans.append(x)
# 按完之後盤面開始變化
            list[x-1] = 0
            for i in range(n) :
                check.append(list[i])
            for i in range(n) :
                if i != x-1 and check[i] != 0:
                    list[i] = list[i] - 1
                    if i != 0 :
                        list[i-1] = list[i-1] + 1
                    if i != n-1 :
                        list[i+1] = list[i+1] + 1 
# 檢查是否已經結束(只剩0)   
            check_fin = 0
            for i in range(n) :
                if list[i] >= 1 :
                    check_fin = check_fin - 1
                    finish = False
                    list[i] = 1
# 結束，return
            if check_fin == 0:
                finish = True
                return
# 還沒結束，檢查此盤面是否出現過
            else :
                check_same = 0
                for i in range(repeat_time) :
# 已重複出現，回到parent
                    if repeat[i] == list :
                        move = move - 1
                        del ans[-1]
                        check_same = -1
                        break
# 未出現過，將盤面紀錄
                if check_same == 0 :        
                    tmp = deepcopy(list)
                    repeat = repeat + [tmp]
                    repeat_time = repeat_time +1
# 還不到最深，再往下
                    if layer != limit :
                        layer = layer + 1
                        ids(list,n)
                        if finish == True :
                            return
# 已經最深的還沒結束，這層的重複盤面pop出來，回到上一層
                    else :
                        repeat.pop()
                        repeat_time = repeat_time -1
                        move = move - 1
                        del ans[-1]
# 還沒結束，回到parent
    if finish == False :
        if(layer > 1):
            repeat.pop()
            repeat_time = repeat_time -1
            move = move - 1
            del ans[-1]
            layer = layer -1
# 重複執行，直到找到解
while 0 == 0 :
    repeat.clear()
    tmp = deepcopy(list_or)
    repeat = repeat + [tmp]
    repeat_time = 1
    layer = 1
    limit = limit + 1
    # print("i = ",limit)
    move = 0
    ans.clear()
    ids(list_or,n)
    if finish == True or no_solution == True:
        break
fp = open("output.txt","w")
if move == 0 :
    lines=["total rum time: ",str(time.time() - start_time)," second\n","There is no solution"]
    fp.writelines(lines)
    exit()
lines=["total rum time: ",str(time.time() - start_time)," second\n","An optimal solution has " ,str(move)," moves :\n",str(ans)]
fp.writelines(lines)
exit()