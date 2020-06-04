N, r, c = map(int, input().split())


# stack을 이용한 DFS를 사용 >> 전체경우 테스트...
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
                return
            continue

        half = sz / 2
        stack.append((half, x + half, y + half))
        stack.append((half, x + half, y))
        stack.append((half, x, y + half))
        stack.append((half, x, y))


# Z(2**N, 0, 0)
import time
start0 = time.time()

for n in range(1, 15):
    start = time.time()
    print("--------","STEP:", n)
    r, c = 2**n - 1, 2**n - 1
    Z(2**n, 0, 0)
    print("time:%.2f" % float(time.time() - start))

print()
print("End:%.2f" % float(time.time() - start))



## 결과
# -------- STEP: 1
# 3
# time:0.00
# -------- STEP: 2
# 15
# time:0.00
# -------- STEP: 3
# 63
# time:0.00
# -------- STEP: 4
# 255
# time:0.00
# -------- STEP: 5
# 1023
# time:0.00
# -------- STEP: 6
# 4095
# time:0.01
# -------- STEP: 7
# 16383
# time:0.02
# -------- STEP: 8
# 65535
# time:0.10
# -------- STEP: 9
# 262143
# time:0.37
# -------- STEP: 10
# 1048575
# time:1.56
# -------- STEP: 11
# 4194303
# time:5.92
# -------- STEP: 12
# 16777215
# time:25.16
# -------- STEP: 13
# 67108863
# time:109.18
# -------- STEP: 14
# 268435455
# time:437.08

# End:437.08
