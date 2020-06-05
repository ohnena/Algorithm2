
# 틀렸다...내가 너무 나이브하게 생각했구나.
# 그냥 모든경우를 계산하는 완전탐색이 답이다..
# 어정쩡하게 최소힙으로 풀생각하지 말고...(틀릴걸 알면서 왜 그렇게 하는건지...나도 날 모르겠네...)
import heapq

N = int(input())
ground = []
for i in range(N):
    row = list(map(int, input().split()))
    ground.append(row)


drx = [0, -1, 0, 1]
dry = [1, 0, -1, 0]
isOccupied = [[False] * N for i in range(N)]



heap_data = []
cost = 0
for i in range(1,N-1):
    for j in range(1,N-1):
        cost = ground[i][j]
        for k in range(4):
            x, y = i+drx[k], j+dry[k]
            cost += ground[x][y]
        heapq.heappush(heap_data,(cost,i,j))



total_cost = 0
cnt = 3
while heap_data and cnt > 0:
    # 최소힙을 팝하고, 
    cost, x, y = heapq.heappop(heap_data)
    # 심을 수 없다면,
    canOccupy = True 
    if isOccupied[x][y]:
        canOccupy = False 
    for i in range(4):
        if isOccupied[x+drx[i]][y+dry[i]]:
            canOccupy = False
            break
    # 심을 수 있다면, 심고 비용합산 
    if canOccupy:
        # print(cost,x,y)
        total_cost += cost
        isOccupied[x][y] = True
        for i in range(4):
            nx, ny = x+drx[i], y+dry[i]
            isOccupied[nx][ny] = True
        # (씨앗을 3개 다 심을때까지 반복)
        cnt -= 1
    

print(total_cost)
# for i in range(N):
#     for j in range(N):
#         print(isOccupied[i][j], end=' ')
#     print()
