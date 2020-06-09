N = int(input())
TRI = [[0]*(N+1) for _ in range(N+1)]
DP = [[0]*(N+1) for _ in range(N+1)]
# 점화식 DP[i][j] = max(DP[i-1][j-1],DP[i-1][j]) + TRI[i][j]
for i in range(1,N+1):
    row = list(map(int, input().split()))
    for j in range(1,i+1):
        TRI[i][j] = row[j-1]

for i in range(1, N+1):
    for j in range(1,i+1):
        DP[i][j] = max(DP[i-1][j-1],DP[i-1][j]) + TRI[i][j]

print(max(DP[N]))