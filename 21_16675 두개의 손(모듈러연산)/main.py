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


def p1_win(p1, p2):
    if (p1 == 'S' and p2 == 'P') or (p1 == 'R'
                                     and p2 == 'S') or (p1 == 'P'
                                                        and p2 == 'R'):
        return True
    else:
        return False


def game(lst):
    #1 무승부 case
    if len(set(lst)) == 1:
        print("?")
        return

    #2 결과 예측불가 case
    if lst[0] != lst[1] and lst[2] != lst[3] and (len(set(lst)) == 3
                                                  or len(set(lst)) == 2):
        print("?")
        return

    #3 누군가는 반드시 이기는 case
    #(한사람은 똑같은걸 내고, 다른 한사람은 이기는 패를 가질때)
    if lst[0] == lst[1]:
        if p1_win(lst[2], lst[0]) or p1_win(lst[3], lst[0]):
            print("TK")
            return

    if lst[2] == lst[3]:
        if p1_win(lst[0], lst[2]) or p1_win(lst[1], lst[2]):
            print("MS")
            return

    print("?")


lst = list(map(str, input().split()))
game(lst)

