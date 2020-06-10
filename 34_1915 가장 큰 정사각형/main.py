N, M = map(int, input().split())
MAP = [[0]*(M+1)] + [[0]+list(map(int, list(input()))) for _ in range(N)] # 좌상단에 0으로 패딩 한줄씩...
DP = [[0]*(M+1) for _ in range(N+1)]

for row in MAP:
    print(row)

# DP[i][j] = (i,j)칸을 최우하단 블록으로 갖는 가능한 정사각형의 최대 넓이
# 하지만 구현에서 실패.
# 
# 해답. (내가 생각한 것과 살짝 다른 아이디어다.)
# DP[i][j] = (i,j)칸을 최우하단 블록으로 갖는 가능한 정사각형의 최대 사이즈(한변의 길이)
# 점화식 DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1]) + MAP[i][j]
for i in range(1, N+1):
    for j in range(1, M+1):
        if MAP[i][j]:
            DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1]) + 1


print("==========")
for row in DP:
    print(row)

print(max([max(row) for row in DP])**2)