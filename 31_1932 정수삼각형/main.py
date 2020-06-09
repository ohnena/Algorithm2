N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]
d = [[0] * (N) for _ in range(N)]
d[0][0] = tri[0][0]

for i in range(N-1): # 층...
    for j in range(i+1):
        #left 처리
        d[i+1][j] = max(d[i+1][j], d[i][j] + tri[i+1][j])
        #right 처리 
        d[i+1][j+1] = max(d[i+1][j+1], d[i][j] + tri[i+1][j+1])

print(max(d[N-1]))

    

    
    
    
