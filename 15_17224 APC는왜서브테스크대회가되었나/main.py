N, M, K = map(int, input().split())
hard, easy = 0, 0
for i in range(N):
    e, h = map(int, input().split())
    if h <= M:
        hard += 1
    elif e <= M:
        easy += 1

result = min(K, hard) * 140
if K > hard:
    result += min(K-hard, easy) * 100 # 은근히 까다로운...

print(result)