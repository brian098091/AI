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
next_f = 1000000
f_limit = 0
#f= g(第幾層) + h(剩餘細胞個數*根號2)
def f(g,h) :
    global f_limit,next_f
    f = g + h
    if f > f_limit :
        next_f = min(next_f,f)
        return False
    else :
        return True
#h = 剩餘細胞個數*根號2        
def heuristic(h) :
    h = h * np.sqrt(2)
    return h
def ida(list_org,n):
    global move,finish,repeat_time,check_fin,repeat,tmp,check_same,limit,layer,no_solution
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
            h = 0
            for i in range(n) :
                if list[i] >= 1 :
                    check_fin = - 1
                    h = h + 1
                    list[i] = 1
            if check_fin == 0:
                finish = True
                return
#檢查可不可以到下一層
            h = heuristic(h)
            next_layer = f(move,h)
# 不行，backtracking
            if next_layer == False :
                move = move - 1
                del ans[-1]
# 可以，往下一層
            else :
                layer = layer + 1
                ida(list,n)
                if finish == True :
                    return
# 還沒結束，回到parent
    if finish == False :
        if(layer > 1):
            move = move - 1
            del ans[-1]
            layer = layer -1
# f_limit 初始化
for i in range(n) :
    if list_or[i] == 1 :
        f_limit = f_limit + 1

# 重複執行，直到找到解
while 1 == 1 :
    layer =1
    # print("i = ",limit)
    move = 0
    ans.clear()
    ida(list_or,n)
    f_limit = deepcopy(next_f)
    next_f = 1000000
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