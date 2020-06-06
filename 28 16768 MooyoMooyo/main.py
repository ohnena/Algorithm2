import sys
sys.setrecursionlimit(100000)  # dfs재귀 사용시에는 이게 포인트...

N, K = map(int, input().split())

board = []
for _ in range(N):
    row = input()
    board.append(list(row))
drx = [0, -1, 0, 1]
dry = [1, 0, -1, 0]

# countRemoved = 0
toRemove = []
checked = [[False] * 10 for _ in range(N)]


def dfs(x, y, adjs):
    global hasRemoved
    checked[x][y] = True
    if len(adjs) == K:
        hasRemoved = True
        # for tp in adjs:
        #     board[tp[0]][tp[1]] = '0'
        toRemove.extend(adjs)
    elif len(adjs) > K:
        toRemove.append((x, y))

    for i in range(4):
        nx = x + drx[i]
        ny = y + dry[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= 10:
            continue
        if board[nx][ny] == board[x][y] and not checked[nx][ny]:
            adjs.append((nx, ny))
            dfs(nx, ny, adjs)
            # adjs.pop()



def search():
    for i in range(N):
        for j in range(10):
            if board[i][j] != '0' and not checked[i][j]:
                dfs(i, j, [(i, j)])


def remove():
    while toRemove:
        x, y = toRemove.pop()
        board[x][y] = '0'


def gravity_():
    # for i in range(N-1,0,-1):
    #     for j in range(10):
    #         if board[i][j] == '0' and board[i-1][j] != '0':
    #             board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
    for i in range(N - 1):
        for j in range(10):
            if board[i][j] != '0' and board[i + 1][j] == '0':
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]


def gravity__():
    # zeroCnt = 0
    nonZeroCnt = 0
    for _ in range(N):
        for i in range(10):
            for j in range(N - 1, 0, -1):
                if board[j][i] == '0' and board[j - 1][i] != '0':
                    board[j][i], board[j - 1][i] = board[j - 1][i], board[j][i]


def gravity():
    for i in range(10):
        temp = []
        for j in range(N):
            if board[j][i] != '0':
                temp.append(board[j][i])
        for j in range(N - len(temp)):
            board[j][i] = '0'
        for j in range(N-len(temp),N):
            board[j][i] = temp[j-N+len(temp)]



def _debugPrint():
    # print()
    for i in range(N):
        print(''.join(board[i]))


hasRemoved = False
while (True):
    # remove() 작업
    checked = [[False] * 10 for _ in range(N)]
    search()
    remove()

    # remove() 작업내역 존재시, gravity() 작업
    if hasRemoved:
        # _debugPrint()
        gravity()
        hasRemoved = False
        # _debugPrint()
        # exit()
    else:
        break

_debugPrint()
