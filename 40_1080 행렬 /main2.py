# 해답

# 3 4
# 0000
# 0010
# 0000
# 1001
# 1011
# 1001



# 조건
# - 연산한번에 3X3 뒤집기 가능
# - 대상은 최대 30X30 행렬

# 행렬뒤집기 함수
def flip(mat, x, y):
    for i in range(3):
        for j in range(3):
            mat[x+i][y+j] ^= 1


            




N, M = map(int, input().split())
MAT1 = [list(map(int, list(input()))) for _ in range(N)]
MAT2 = [list(map(int, list(input()))) for _ in range(N)]



cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if MAT1[i][j] != MAT2[i][j]:
            flip(MAT1, i, j)
            cnt += 1

if MAT1 == MAT2:
    print(cnt)
else:
    print(-1)







