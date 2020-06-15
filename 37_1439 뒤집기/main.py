# 합격
S = list(input())

state = ''
cnt_one = 0
cnt_zero = 0
for i in range(len(S)):
    if S[i] != state:
        if state == '0':
            cnt_zero += 1
        elif state == '1':
            cnt_one += 1
        state = S[i] 

    if i == len(S)-1 :
        if state == '0':
            cnt_zero += 1
        elif state == '1':
            cnt_one += 1
print(min(cnt_one, cnt_zero))

        
