# 0: 정보과학관 < 12
# 1: 전산관 <023
# 2: 미래관 < 0135
# 3: 신양관 < 1245
# 4: 진리관 < 356
# 5: 한경직기념관 < 2347
# 6: 학생회관 < 47
# 7: 형남공학관 < 56

# DP = 0분에 어떤 지점에 도착할 수 있는 상태
DP = [1,0,0,0,0,0,0,0]
G = [[1,2],
    [0,2,3],
    [0,1,3,4],
    [1,2,4,5],
    [2,3,5,7],
    [3,4,6],
    [5,7],
    [4,6]]


def nxt(state):
    tmp = [0 for _ in range(8)]
    for i in range(8):
        for n in G[i]:
            tmp[i] += state[n]
        tmp[i] %= 1000000007
    return tmp
    # tmp[0] = state[1] + state[2]
    # tmp[1] = state[0] + ... 그냥 위의 반복문으로 대체...

for i in range(int(input())):
    # print(i,"sec: ",DP)
    DP = nxt(DP)
print(DP[0])