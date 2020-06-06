
# -해답 해설 : 과정이 꽤나 직관적이다. dfs1돌아서 지울걸 찾은다음, dfs2를 돌며 질울걸 지워버리고, gravity()로 테트리스처리

# hasRemoved = False
# ret = dfs1(x,y)            //x,y를 시작으로해서 만들어지는 그룹의 원소 개수
# if ret>=K:
#  	dfs2(x,y,board[x][y]) //위에서 받은 ret이 >=K이면, 그룹의 원소 모두를 '0'(공백)으로 치환.
#  	hasRemoved = True
# if hasRemoved:
#  	gravity()처리             // 테트리스처럼 공백을 위의 무언가로 채워넣기
# hasRemoved = False

# - (위의 세가지 프로세스를, 무한루프)
import sys
sys.setrecursionlimit(100000)  # dfs재귀 사용시에는 이게 포인트...

N, K = map(int, input().split())

board = []
for _ in range(N):
    row = input()
    board.append(list(row))
drx = [0, -1, 0, 1]
dry = [1, 0, -1, 0]


checked = [[False] * 10 for _ in range(N)]



def dfs1(x,y):
    checked[x][y] = True
    ret = 1
    for i in range(4):
        nx = x + drx[i]
        ny = y + dry[i]
        if nx < 0 or nx >= N or ny <0 or ny >= 10:
            continue
        if board[nx][ny] == board[x][y] and not checked[nx][ny]:
            ret += dfs1(nx, ny)
    return ret

def dfs2(x,y,val):
    checked[x][y] = True
    board[x][y] = '0'
    for i in range(4):
        nx = x + drx[i]
        ny = y + dry[i]
        if nx < 0 or nx >= N or ny <0 or ny >= 10:
            continue
        if board[nx][ny] == val and not checked[nx][ny]:
            dfs2(nx, ny, val)

def create_newChecked():
    global checked
    checked = [[False] * 10 for _ in range(N)]

def search_remove():
    global hasRemoved
    for i in range(N):
        for j in range(10):
            if board[i][j] != '0' and not checked[i][j]:
                create_newChecked()
                ret = dfs1(i,j)
                if ret >= K:
                    # print(board[i][j],ret)
                    # _debugPrint()
                    create_newChecked()
                    dfs2(i,j,board[i][j])
                    # print()
                    # _debugPrint()
                    # exit()
                    hasRemoved = True


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
    ## remove() 작업
    # checked = [[False] * 10 for _ in range(N)]
    # search()
    # remove()
    search_remove()



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
