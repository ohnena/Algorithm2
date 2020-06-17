# 더빠른 솔루션
# 중복되는 값들을 애초에 넣지 않도록 하여, set체크의 부하를 없앴다
# (참고: https://mygumi.tistory.com/183)

from sys import stdin
from copy import deepcopy
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

k, n = map(int, read().split())
arr = list(map(int, read().split()))
hq = deepcopy(arr)

for i in range(n-1):
    cur = heappop(hq)
    for j in arr:
        heappush(hq, cur * j)
        if cur % j == 0: break # 중복되는 값을 배제...

print(heappop(hq))