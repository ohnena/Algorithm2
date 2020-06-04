def score(lst):

    if len(set(lst)) == 1:
        return 50000 + lst[0] * 5000
    if len(set(lst)) == 2:
        lst.sort()
        if lst[1] == lst[2]:
            return 10000 + lst[1] * 1000
        else:
            return 2000 + lst[1] * 500 + lst[2] * 500
    
    lst.sort()
    for i in range(3):
        if lst[i] == lst[i + 1]:
            return 1000 + 100 * lst[i]

    return max(lst) * 100


result = 0
for _ in range(int(input())):
    cand = list(map(int, input().split()))
    result = max(result, score(cand))
print(result)

# 소회
# :
# 이런식의 장황한 조건문을 짤때는 반드시
# 헛점이 없는지를 주의해서 체크해야!
# 즉 논리적으로 명확해야한다.