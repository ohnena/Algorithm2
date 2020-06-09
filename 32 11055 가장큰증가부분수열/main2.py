N = int(input())
S = list(map(int, input().split()))
DP = [0] * N
DP[0] = S[0]
rev = [0] * N
# 점화식 DP[i] = S[i] + min(DP[j]) (j는 0<=j<i and S[j] < S[i])



for i in range(N):
    val = 0
    rev_p = 0
    for j in range(i):
        if S[j] < S[i]:
            if val < DP[j] :
                rev_p = j
            val = max(val, DP[j])  

    DP[i] = S[i] + val
    rev[i] = rev_p

print(max(DP))



# 히스토리 출력 방식 1 (좀더 스마트...)
print("=====")
target = max(DP)
while target > 0:
    for i in range(N):
        if DP[i] == target:
            print(S[i])
            target = DP[i] - S[i]
            break

# 히스토리 출력 방식 2 (rev가 필요)
print("=====")
target_i = 0
for i in range(N):
    if DP[i] == max(DP):
        target_i = i
i = target_i
while rev[i] != i:
    print(S[i])
    i = rev[i]
print(S[i])

