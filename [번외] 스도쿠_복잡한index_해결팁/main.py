a=input()

cnt = 0
board = [[0]*9 for i in range(9)]
for j in range(9):
    for k in range(9):
        x = j//3*3 + k//3
        y = j%3*3 + k%3
        # print(j,k,x,y)
        board[x][y] = cnt
        cnt += 1


for j in range(9):
    for k in range(9):
        print("%2d"%board[j][k], end=' ')
    print()

