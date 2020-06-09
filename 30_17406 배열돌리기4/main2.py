
import copy 
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] #남,서,북,동

ans = float('inf') #//전역변수, 최대값으로 초기화...

def _debugPrint(arr):
    print("=======")
    for row in arr:
        print(row)

def value(arr): #//배열의 최소결과값
    return min([sum(row) for row in arr])
def convert(arr, qry): #//중심점을 기준으로 한칸씩 회전...
    
    r, c , s = qry
    narr = copy.deepcopy(arr)

    for i in range(1, s+1): #우상향 대각선 점들에 대한 루프
        rr, cc = r-1-i, c-1+i
        for j in range(4): #남서북동 개별 방향에 대한 처리 루프
            for _ in range(i*2):
                rrr, ccc = rr+dx[j], cc+dy[j]
                narr[rrr][ccc] = arr[rr][cc] # arr > narr
                rr, cc = rrr, ccc
    return narr

# def dfs(arr, status): #//백트래킹
#     global ans
#     if sum(status) == K: # 비트마스킹 흉내...
#         ans = min(ans, value(arr))
#         return
#     for i in range(K):
#         if status[i]:
#             continue
#         narr = convert(arr, Q[i])
#         status[i] = 1
#         dfs(narr, status)
#         status[i] = 0
# dfs(A, [0 for i in range(K)]) 
# print(ans)


# 진짜 비트마스킹...(위는 흉내)
def dfs(arr, status): #//백트래킹
    if status == (1<<K)-1: # 비트마스킹 흉내...
        return value(arr)
    
    ret = float('inf')
    for i in range(K):
        # if status[i]:
        if status&(1 << i): 
            continue
        narr = convert(arr, Q[i])
        ret = min(ret, dfs(narr, status|(1 << i)))
    return ret
print(dfs(A, 0))





