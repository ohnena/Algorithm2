# BOJ 9037 The candy war
def need_keep(n, candy):
    for i in range(n):
        if candy[i] % 2 != 0:
            candy[i] += 1
    return len(set(candy)) != 1 # 코딩팁...

    
def teacher(n, candy):
    give = [0] * n 
    for i in range(n):
        give[i] = candy[i] // 2
        candy[i] = give[i]
    for i in range(n):
        candy[(i+1)%n] += give[i] # 인덱스 사용팁...


def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    while need_keep(N, candy):
        cnt += 1
        teacher(N, candy)
    print(cnt)
     
    
for _ in range(int(input())):
    process()