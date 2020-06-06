# BOJ 1012, FloodFill의 대표유형 

# # dfs
# - dfs구현은 조금 꺼려진다. 밭의 가로세로가 최대 50이라서, 2500번의 dfs를 구행해야할 수도 있다.
# - 만약 구현한다면, dfs(start_x, start_y, [])로 해야겠다. 마지막인자인 lst는 해당회차의 방문그룹을 관리해서,
# 막다른길에서, 재귀리턴하기전에 기록하기 위함이다
# # bfs
# - 우선 bfs니까 deque를 이용하겠다. 생각해보니, dfs나 bfs모두 N*N 매번 실행해줘야할테니,
# 굳이 방문그룹을 기록해둘 필요가있을까? bfs가 오히려 더 깔끔할 것 같다.

# dfs, bfs 모두 구현 


N = int(input())
drx = [0,-1,0,1]
dry = [1,0,-1,0]

# 디버깅용...
def printDebug(lst):
    for i in range(R):
        for j in range(C):
            # print(MAP[i][j], end='')
            print(lst[i][j], end=' ')
        print()



import sys
sys.setrecursionlimit(100000) # dfs재귀 사용시에는 이게 포인트... 
def dfs(x, y): # recusrion_limit 설정 필요...
    if visited[x][y] or MAP[x][y] != 1:
        return

    visited[x][y] = True

    for i in range(4):
        nx = x + drx[i]
        ny = y + dry[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if not visited[nx][ny] and MAP[nx][ny] == 1:
            dfs(nx,ny)


def bfs(start_x, start_y):
    q = [(start_x, start_y)] #deque([(start_x,start_y)])
    
    while q:
        x, y = q.pop() #q.popLeft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for i in range(4):
            nx = x + drx[i]
            ny = y + dry[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if MAP[nx][ny] == 1:
                q.append((nx,ny))


for _ in range(N):

    R, C, K = map(int, input().split())
    MAP = [[0]*C for _ in range(R)]
    for i in range(K):
        x, y = map(int, input().split())
        MAP[x][y] = 1
    visited = [[False]*C for _ in range(R)]

    

    cnt = 0
    for i in range(R):
        for j in range(C):
            if not visited[i][j] and MAP[i][j] == 1:
                bfs(i,j)            
                # dfs(i,j)
                cnt += 1
                # print(i,j)
                # printDebug(visited)
                # exit()

    print(cnt)



        


