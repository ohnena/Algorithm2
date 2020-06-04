# 입력
# 첫 번째 줄에 차례로 ML, MR, TL, TR이 공백으로 구분되어 주어진다. 차례대로 민성이의 왼손과 오른손, 태경이의 왼손과 오른손의 상태를 나타낸다.

# 위 4개의 값들은 “S”, “R”, “P” 중 하나이며, 각각 가위, 바위, 보를 의미한다.

# 출력
# 첫 번째 줄에 민성이가 무조건 이길 수 있다면 “MS”,
# 태경이가 무조건 이길 수 있다면 “TK”,
# 누가 이길 지 확답할 수 없다면 “?”를
# 쌍따옴표를 제외하고 출력한다.

# 가위바위보에서 가위는 보를 이기고,
# 바위는 가위를 이기며,
# 보는 바위를 이긴다.
# 같은 손동작끼리는 승부가 나지 않는다 (비긴다).

ML, MR, TL, TR = ('SPR'.index(c) for c in input().split()) # index()아닌 find()도 가능...

# 어느 한쪽이 반드시 이기는 경우는 한가지다. 
# 한쪽이 같은걸 내고, 다른 한쪽이 거기에 이기는 패를 가질때.
if ML == MR and (MR+2) % 3 in [TL, TR]: 
    print("TK")
elif TL == TR and (TR+2) % 3 in [ML, MR]:
    print("MS")
else:
    print("?")

# 이렇게
# 가위바위보와 같이 사이클이 있는 경우,
# %연산을 사용하면 좋다