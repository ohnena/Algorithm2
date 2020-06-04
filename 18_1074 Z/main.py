N, r, c=map(int,input().split())

cnt = -1
# 재귀적 구현...
def Z(sz,x,y):
    global cnt 
    if sz == 1:
        cnt += 1
        if x== r and y==c:
            print(cnt)
            exit()
        return
    for i in range(2):
        for j in range(2):
            _x = sz/2 * i + x
            _y = sz/2 * j + y 
            Z(sz/2,_x,_y)
            # print("%2d%2d" % (_x,_y), end=' ')
        # print()

Z(2**N,0,0)
