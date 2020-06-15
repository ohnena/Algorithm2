# DP로 어떻게 접근해야할지 아이디어 탐색에 실패 ㅠㅠ 
# 그래서 그냥 무식하게 풀어보았다. 물론 시간초과...
# 너무 무식해서 이렇다 설명할게 없다...


G = [[1,2],
    [0,2,3],
    [0,1,3,4],
    [1,2,4,5],
    [2,3,5,7],
    [3,4,6],
    [5,7],
    [4,6]]
V = len(G)
D = int(input())
DP = [[0]*(D) for _ in range(V)]
# DP[x][t] = x에 t초만에 가는 경로수
# DP[0][D] = DP[]

ans = 0
def bfs(start, DUR):
    ret = 0
    stack = []
    stack.append((0, start))
    while stack:
        ct, cv = stack.pop()
        if ct >= DUR:
            if ct == DUR and cv == start:
                ret += 1
                ret %= 1000000007
            continue
        for nv in G[cv]:
            stack.append((ct+1,nv))
    return ret


print(bfs(0, D))





