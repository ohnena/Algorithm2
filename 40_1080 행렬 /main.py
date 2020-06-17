# 광탈

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

# 행렬비교 함수
def isEqual(mat1, mat2): 
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            if mat1[i][j] != mat2[i][j]:
                return False
    return True

def compare(mat1, mat2, x, y):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if mat1[x+i][y+j] != mat2[x+i][y+j]:
                cnt += 1
    return cnt#/(3*3)

    


import copy
def convert(mat, x, y):
    nmat = copy.deepcopy(mat)
    for i in range(3):
        for j in range(3):
            nmat[x+i][y+j] ^= 1
    return nmat


def calc(mat1, mat2, converted):
    rlst = []    
    for i in range(len(mat1)-2):
        for j in range(len(mat1[0])-2):
            if (i,j) in converted:
                continue
            cnt = compare(mat1, mat2, i, j)
            if cnt > 0:
                rlst.append((cnt, i, j))                
    if len(rlst) > 0:
        sorted(rlst, key = lambda data: data[0], reverse=True)
    return rlst
            
            




N, M = map(int, input().split())
MAT1 = [[0]*M for _ in range(N)]
MAT2 = [[0]*M for _ in range(N)]
tip = [[0]*M for _ in range(N)]
# MAT1 = [list(input()) for _ in range(N)]
# MAT2 = [list(input()) for _ in range(N)]
for i in range(N):
    srow = input()
    for j in range(len(srow)):
        if srow[j] == '1':
            MAT1[i][j] = 1
for i in range(N):
    srow = input()
    for j in range(len(srow)):
        if srow[j] == '1':
            MAT2[i][j] = 1


cnt = 0
tmat = MAT1
converted = []
while (True):
    tip = calc(tmat,MAT2, converted)
    if len(tip) > 0:
        x, y = tip[0][1], tip[0][2]
        tmat = convert(tmat, x, y)
        converted.append((x,y))
        cnt += 1
        if isEqual(tmat, MAT2):
            print(cnt)
            exit()
        if isEqual(tmat, MAT1):
            print(-1)
            exit()
    
        







