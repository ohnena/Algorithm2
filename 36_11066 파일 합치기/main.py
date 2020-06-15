## 엄청어렵다...결국 해답으로 바로...
## 강사왈: 이건 처음보면 절대 DP를 구할 수 없다고. 유형의 문제라서.


## 핵심아이디어 (점화식)
# DP[i][j]: i부터 j까지 합하는데 드는 최소 비용
# DP[i][j] = min(DP[i][k] + DP[k+1][j]) + sum(A[i] ~ A[j])  (k는 i ~ j-1)
# ex) <30, 40> : 0 + 0 + (30+40)
# <40, 30, 30, 50> : <40,30> + <30,50> + (40+30+30+50)



def process():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    S = [0] * (N+1)
    for i in range(1, N+1):
        S[i] += S[i-1] + A[i] 
    DP = [[0] * (N+1) for _ in range(N+1)]
    for i in range(2, N+1): # 부분파일의 길이 
        for j in range(1, N+2-i): # 시작점
            DP[j][j-1+i] = min([DP[j][j+k] + DP[j+k+1][j-1+i] for k in range(i-1)]) + (S[j-1+i] - S[j-1])
    print(DP[1][N])


for _ in range(int(input())):
    process()
    
