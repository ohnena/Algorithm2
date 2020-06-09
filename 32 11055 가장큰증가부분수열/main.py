N = int(input())
S = list(map(int, input().split()))
DP = [0] * N
DP[0] = S[0]
# 점화식 DP[i] = S[i] + min(DP[j]) (j는 0<=j<i and S[j] < S[i])



for i in range(N):
    val = 0
    for j in range(i):
        if S[j] < S[i]:
            val = max(val, DP[j])
    DP[i] = S[i] + val

print(max(DP))