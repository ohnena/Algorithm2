N, r, c = map(int, input().split())


# stack을 이용한 DFS를 사용
def Z(sz, x, y):
    cnt = -1
    stack = []
    half = sz / 2
    stack.append((half, x + half, y + half))
    stack.append((half, x + half, y))
    stack.append((half, x, y + half))
    stack.append((half, x, y))

    while stack:
        sz, x, y = stack.pop()
        if sz == 1:
            cnt += 1
            if x == r and y == c:
                print(cnt)
                # exit()
            continue

        half = sz / 2
        stack.append((half, x + half, y + half))
        stack.append((half, x + half, y))
        stack.append((half, x, y + half))
        stack.append((half, x, y))


Z(2**N, 0, 0)


