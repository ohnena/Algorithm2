
# DFS재귀를 이용하여 완전탐색으로 다시 풀어보자.
# 파이썬이라서...걱정이 되긴하네...
# 성공!!!! >> 다행히 재귀의 깊이가 3밖에 안되니 가능한듯...휴...




# 소회
# :
# 처음엔 그냥 꼼수를 생각했다. bfs에서 (1~N-1)*(1~N-1)의 
# costSum들을 모두 구한다음, heapq로 가장 작은 거부터 pop해가며
# 겹치지 않는 거 3개를 찾는다. 즉 모든경우를 고려하지 않았다.

# 당연히 코딩하면서도, 꺼림찍했다. 논리적으로 너무 빈약했기때문이다.
# 물론 결과도 실패.

# 그래서 풀이를 좀 찾아봤다. (강의에선 너무 난해한 풀이를 사용해서다. N*N루프를 3중으로 돌리는...)
# 그런데 아니나다를까, 이문제는 재귀dfs에다가 심지어 완전탐색까지 써야하는 
# 문제였다. 본능적으로 재귀dfs에는 거부감이 드는게 사실이다. 그런데 거기에 완전탐색까지 해야한다니
# 이게 어떻게 가능한걸까 어이가 없었다.

# 그런데 이렇게 코딩을 마치고나니, 내가 생각하지 못한 지점이있었다.
# 바로 재귀의 깊이가 최대 3층까지라는 것이다. 생각해보니 그러면 재귀도 해볼만 하겠구나 싶었다.

# 어쩐지 합격률이 높더라. 오늘도 어김없이 삽질은 했지만, 교훈을 얻어서 나름 의미가 있다.

# <오늘의 교훈> : 재귀의 깊이가 낮을땐, dfs재귀+완전탐색도 써볼만하구나!



N = int(input())
ground = []
for i in range(N):
    row = list(map(int, input().split()))
    ground.append(row)

drx = [0, 0, -1, 0, 1] #편의를 위해 (0,0)도 포함...
dry = [0, 1, 0, -1, 0]
isOccupied = [[False] * N for _ in range(N)]

costSums = [[0]*N for _ in range(N)]
for i in range(1, N-1):
    for j in range(1, N-1):
        for k in range(5):
            costSums[i][j] += ground[i+drx[k]][j+dry[k]]

# 디버깅용...
# def printList(lst, n):
#     for i in range(n):
#         for j in range(n):
#             print(lst[i][j], end=' ')
#         print()


def isSecure(x,y):
    for i in range(5):
        if isOccupied[x+drx[i]][y+dry[i]]:
            return False
    return True
        

result_cost = float('inf')
# cnt는 씨앗수
def dfs(x, y, cnt, csum):
    global result_cost
    # 재귀 탈출...
    if cnt == 3:
        # print(cnt, result_cost, csum)
        result_cost = min(result_cost, csum)
        max_cost = max(max_cost, csum)
        return

    # # 재귀 진입할지 체크...
    # for i in range(5):
    #     if isOccupied[x+drx[i]][y+dry[i]]:
    #         return

    # 재귀전 방문체크
    for i in range(5):
        isOccupied[x+drx[i]][y+dry[i]] = True
    
    # 재귀 돌입
    for i in range(1,N-1):
        for j in range(1,N-1):
            if isSecure(i,j): # 재귀 진입 가능여부 체크...
                dfs(i,j, cnt+1, csum+costSums[i][j])

    # 재귀후 방문해제
    for i in range(5):
        isOccupied[x+drx[i]][y+dry[i]] = False






for i in range(1, N-1):
    for j in range(1, N-1):
        dfs(i,j,1,costSums[i][j])





print(result_cost)