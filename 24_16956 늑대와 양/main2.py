# 참 골때리는 문제다. 조금 어이가 없다. 이거가지고 삽질했다니...
# 내 결점이 여실히 들어나버리는구나. 괜히 어렵게 생각했어.
# 이문제는 그냥 울타리는 어떻게 설치하든 상관없으니, 늑대로부터 양만 보호하면된다.
# 양과 늑대의 이동권을 보장하지 않아도 되니, 그냥 그 칸에 가둬버렸다.
# 나참...

R, C = map(int,input().split())
board = [list(input()) for _ in range(R)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

isAdjacent = False
for i in range(R):
    for j in range(C):
        if board[i][j] == 'W':
            for k in range(4):
                x, y = i+dx[k], j+dy[k]
                if x < 0 or x >= R or y < 0 or y >= C:
                    continue
                if board[x][y] == 'S':
                    isAdjacent = True 
                    break

if isAdjacent:
    print(0)
    exit()
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'D'
            print(board[i][j], end='')
        print()