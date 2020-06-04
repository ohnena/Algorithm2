# 17389 보너스 점수

N, S = int(input()), input()

bonus = 0
score = 0

for idx, c in enumerate(S): # enumerate()사용...
    if c == 'O':
        score, bonus = score + (idx + 1) + bonus, bonus + 1
    if c == 'X':        
        bonus = 0
    
print(score)