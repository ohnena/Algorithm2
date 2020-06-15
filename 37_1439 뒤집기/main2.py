# 해답
# 규칙: (순회중 바뀌는 횟수+1) // 2 가 답이다.
S = input()
cnt = 0
for i in range(1,len(S)):
    if S[i-1] != S[i]:
        cnt += 1
print((cnt+1)//2)