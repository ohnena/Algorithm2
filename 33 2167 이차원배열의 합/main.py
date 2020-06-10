# 9만 * 1만의 시간복잡도...9억 >> 반복문아닌 DP사용해야!

N, M = map(int, input().split())
MAP = [] # 편의를 위해 0값의 패딩을 좌상으로 한줄씩...(MAP,DP)
for i in range(N+1):
    if i == 0:
        MAP.append([0]*(M+1))
        continue
    row = [0] + list(map(int, input().split()))
    MAP.append(row)
K = int(input())
Q = [list(map(int, input().split())) for _ in range(K)]

DP = [[0] * (M+1) for _ in range(N+1)]
# # 점화식 DP[i][j] = DP[i][j-1] + MAP[i][j] (즉 MAP[i][0] 부터 MAP[i][j]까지의 합)
# #    단, (j=0일때) DP[i][0] = MAP[i][0]



def _debugPrint(lst):
    print("=============")
    for row in lst:
        print(row)



# DP(누적합) 세팅
for i in range(N+1):
    for j in range(M+1):
        DP[i][j] = MAP[i][j] + DP[i][j - 1]



for qry in Q:
    i, j, x, y = qry
    
    result = 0
    for k in range(i,x+1):
        result += DP[k][y] - DP[k][j-1]
    print(result)



    
