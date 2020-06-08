# 조건
# 1 같은값이면 충돌시 하나로 합쳐진다 (단, 1회이동에 1블록당 1회결합만 허용)
# 2 이동시 전부 한쪽으로 몰아버린다. (이과정에서 충돌하면 결합)
#   정확히는 블록에 압박이 가해지면 결합된다. (한쪽벽에서 충돌되어 발생한 힘은 반대편끝까지 순차적으로 전달된다.)
# 3 1<=N<=20, 2<=K는2의제곱<=1024, 블록은 적어도 1개 주어진다, 빈칸은 0이 주어진다.

# 목표
# 최대5번이동시켜서 얻을 수 있는 가장 큰 블록 출력





N = int(input())
myboard = []
for _ in range(N):
    row = list(map(int, input().split()))
    myboard.append(row)

def _debugPrint(lst):
    for row in lst:
        print(row)



import copy
def moveE(cur_board):
    board = copy.deepcopy(cur_board)

    # 오른쪽이동
    # 1차이동
    for i in range(N):
        temp_lst = []
        for cell in board[i]:
            if cell != 0:
                temp_lst.append(cell)
        if len(board[i]) == len(temp_lst):
            continue
        for j in range(N-len(temp_lst)):
            board[i][j] = 0
        for j in range(N-len(temp_lst), N):
            board[i][j] = temp_lst[j-(N-len(temp_lst))]

    # 충돌처리
    for i in range(N):
        for j in range(N-1,0,-1):
            if board[i][j] == 0:
                continue
            if board[i][j] == board[i][j-1]:
                board[i][j] += board[i][j-1]
                board[i][j-1] = 0

    # 2차이동
    for i in range(N):
        temp_lst = []
        for cell in board[i]:
            if cell != 0:
                temp_lst.append(cell)
        if len(board[i]) == len(temp_lst):
            continue
        for j in range(N-len(temp_lst)):
            board[i][j] = 0
        for j in range(N-len(temp_lst), N):
            board[i][j] = temp_lst[j-(N-len(temp_lst))]

    return board
    



def moveN(cur_board):
    board = copy.deepcopy(cur_board)
    # 위쪽이동
    # 1차이동
    for i in range(N):
        temp_lst = []
        for j in range(N):
            if board[j][i] != 0:
                temp_lst.append(board[j][i])
        if len(board[i]) == len(temp_lst):
            continue
        for j in range(len(temp_lst)):
            board[j][i] = temp_lst[j]
        for j in range(len(temp_lst),N):
            board[j][i] = 0

    # 충돌처리
    for i in range(N):
        for j in range(N-1):
            if board[j][i] == 0:
                continue
            if board[j][i] == board[j+1][i]:
                board[j][i] += board[j+1][i]
                board[j+1][i] = 0

    # 2차이동
    for i in range(N):
        temp_lst = []
        for j in range(N):
            if board[j][i] != 0:
                temp_lst.append(board[j][i])
        if len(board[i]) == len(temp_lst):
            continue
        for j in range(len(temp_lst)):
            board[j][i] = temp_lst[j]
        for j in range(len(temp_lst),N):
            board[j][i] = 0

    return board
    
def moveW(cur_board):
    board = copy.deepcopy(cur_board)
    # 왼쪽이동
    # 1차이동
    for i in range(N):
        temp_lst = []
        for cell in board[i]:
            if cell != 0:
                temp_lst.append(cell)
        if len(board[i]) == len(temp_lst):
            continue
        for j in range(len(temp_lst)):
            board[i][j] = temp_lst[j]
        for j in range(len(temp_lst),N):
            board[i][j] = 0

    # 충돌처리
    for i in range(N):
        for j in range(N-1):
            if board[i][j] == 0:
                continue
            if board[i][j] == board[i][j+1]:
                board[i][j] += board[i][j+1]
                board[i][j+1] = 0
    
    # 2차이동
    for i in range(N):
        temp_lst = []
        for cell in board[i]:
            if cell != 0:
                temp_lst.append(cell)
        if len(board[i]) == len(temp_lst):
            continue
        for j in range(len(temp_lst)):
            board[i][j] = temp_lst[j]
        for j in range(len(temp_lst),N):
            board[i][j] = 0

    return board



def moveS(cur_board):
    board = copy.deepcopy(cur_board)
    # 아래쪽이동
    # 1차이동
    for i in range(N):
        temp_lst = []
        for j in range(N):
            if board[j][i] != 0:
                temp_lst.append(board[j][i])
        if len(board[i]) == len(temp_lst):
            continue
        for j in range(N-len(temp_lst)):
            board[j][i] = 0
        for j in range(N-len(temp_lst),N):
            board[j][i] = temp_lst[j-(N-len(temp_lst))]            

    # 충돌처리
    for i in range(N):
        for j in range(N-1,0,-1):
            if board[j][i] == 0:
                continue
            if board[j][i] == board[j-1][i]:
                board[j][i] += board[j-1][i]
                board[j-1][i] = 0

    # 2차이동
    for i in range(N):
        temp_lst = []
        for j in range(N):
            if board[j][i] != 0:
                temp_lst.append(board[j][i])
        if len(board[i]) == len(temp_lst):
            continue
        for j in range(N-len(temp_lst)):
            board[j][i] = 0
        for j in range(N-len(temp_lst),N):
            board[j][i] = temp_lst[j-(N-len(temp_lst))]
    
    return board




directions = ['E','N','W','S']

def move(drc, cur_board):
    if drc == 'E':
        return moveE(cur_board)
    elif drc == 'N':
        return moveN(cur_board)
    elif drc == 'W':
        return moveW(cur_board)
    elif drc == 'S':
        return moveS(cur_board)
    else:
        print("can'n find Direction")
        exit()
    




biggest = 0

def getBiggest(lst):
    val = 0
    for row in lst:
        val = max(val, max(row))
    return val
    # return max(max(lst))

def dfs(cnt, drct, cur_board):
    global biggest
    if cnt == 5:
        biggest = max(getBiggest(cur_board), biggest)
        return
    moved_board = move(drct,cur_board)
    for i in range(4):
        dfs(cnt+1,directions[i], moved_board)



for i in range(4):
    dfs(0,directions[i],myboard)

print(biggest)




