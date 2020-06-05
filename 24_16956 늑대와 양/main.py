# 소회
# : 
# 문제의 이해가 중요하다. 삽질했거든
# "이 문제는 그냥 울타리를 설치하자"가 끝이다. 즉 
# 울타리는 어떻게 설치해도 좋으니, 늑대만 접근못하게 하면된다는 것이다.
# 강사는 그냥 브루트포스로 늑대와양을 제외한 칸에는 모두 울타리를 설치해버리더라
# 참 골때리는 문제구나..

R, C = map(int,input().split())

board = [[] for _ in range(R)]
wolves = []
for i in range(R):
    row = input()
    for j in range(C):
        board[i].append(row[j])


    
def canMove(nx,ny):
    if (nx < 0 or nx >= R) or (ny < 0 or ny >= C ):
       return False
    return True 

def printBoard():
    for i in range(R):
        for j in range(C):
            print(board[i][j], end='')
        print()

# from collections import deque
dx = [0,-1,0,1]
dy = [1,0,-1,0]
# def bfs(sx,sy):
#     global board
#     q = [(sx,sy,sx,sy)]#deque([(sx,sy,sx,sy)])
#     visited = [[False]*C for _ in range(R)]
#     while q:
#         x, y, pre_x, pre_y = q.pop() #q.popLeft()
#         if board[x][y] == 'S':
#             board[pre_x][pre_y] = 'D'
#             continue
#         if visited[x][y] == True:
#             continue
#         visited[x][y] = True
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if not canMove(nx, ny):
#                 continue
#             q.append((nx,ny,x,y))
    



for i in range(R):
    for j in range(C):
        if board[i][j] == 'W':
            wolves.append((i,j))




isAdjacent = False
for x,y in wolves:
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not canMove(nx,ny):
            continue
        if board[nx][ny] == 'S':
            isAdjacent = True
            break

if isAdjacent:
    print(0)
    # printBoard()
    exit()

def fill():
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'D'


for x,y in wolves:
    # bfs(x,y)
    fill()

result = 0
for i in range(R):
    if 'D' in board[i]:
        result = 1
        break

print(result)
printBoard()
        


    



            

