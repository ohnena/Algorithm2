N, M, K = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]
rop = [list(map(int, input().split())) for _ in range(K)]
spoint = []
epoint = []
for op in rop:
    r,c,s = op[0], op[1], op[2]
    sx, sy = r-s-1, c-s-1
    ex, ey = r+s-1, c+s-1
    spoint.append((sx,sy))
    epoint.append((ex,ey))
# N, M, K, board, spoint, epoint



def _debugPrint(Board):
    print("===========")
    for row in Board:
        print(row)

import copy
def rotateOutside(N, M, Board, sp, ep):
    
    # 재귀탈출...
    sx,sy,ex,ey = sp[0],sp[1],ep[0],ep[1]
    if sx == ex or sy == ey:
        return Board
    
    # rotate outside...
    nBoard = [[101]*M for _ in range(N)] # Mask...
    rLen = ey - sy + 1
    cLen = ex - sx + 1 
    for i in range(cLen-1):
        nBoard[sx][sy+i+1] = Board[sx][sy+i] # N
        nBoard[ex][sy+i] = Board[ex][sy+i+1] # S
    for i in range(rLen-1):
        nBoard[sx+i+1][ey] = Board[sx+i][ey] # E
        nBoard[sx+i][sy] = Board[sx+i+1][sy] # W
    for i in range(N):
        for j in range(M):
            if nBoard[i][j] <= 100:
                Board[i][j] = nBoard[i][j]
    
    # 재귀
    nsx = sx + 1
    nsy = sy + 1
    nex = ex - 1
    ney = ey - 1
    if nsx < ex and nsy < ey and nex > sx and ney > sy:
        Board = rotateOutside(N, M, Board, (nsx,nsy), (nex,ney))
    
    return Board
    


array = [i for i in range(K)]
order = []
result = []
import copy
def combination(array, length):
    if len(order) == length:
        # print(order)
        result.append(copy.deepcopy(order))
        return

    for i in array:
        if i in order:
            continue
        order.append(i)
        combination(array, length)
        order.pop()


def getMin(Board):
    return min([sum(row) for row in Board])


# 조합생성 후, 순회하며 min값찾기
combination(array,len(array))
val = float('inf')
for order in result:
    myboard = copy.deepcopy(board)
    for i in order:
        myboard = rotateOutside(N, M, myboard, spoint[i], epoint[i])
    val = min(val, getMin(myboard))

print(val)

        
    
        

        

    


