# 이번엔 합집합=A+B-교집합 공식으로 구현해보자...

N, M = map(int, input().split())
MAP = [] # 편의를 위해 0값의 패딩을 좌상으로 한줄씩...(MAP,DP)
for i in range(N+1):
    if i == 0:
        MAP.append([0]*(M+1))
        continue
    row = [0] + list(map(int, input().split()))
    MAP.append(row)

DP = [[0] * (M+1) for _ in range(N+1)]
# # 점화식 DP[i][j] = 모든 MAP(x,y)의 합 (단, 1<=x<=i, 1<=y<=j)



def _debugPrint(lst):
    print("=============")
    for row in lst:
        print(row)



# DP(누적합) 세팅
for i in range(1,N+1):
    for j in range(1,M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + MAP[i][j]


# _debugPrint(MAP)
# _debugPrint(DP)

for _ in range(int(input())):
    i, j, x, y = map(int,input().split())
    print(DP[x][y] - DP[x][j-1] - DP[i-1][y] + DP[i-1][j-1])
    



    
