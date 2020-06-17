import copy
import heapq

K, N = map(int, input().split())
plist = list(map(int, input().split()))


heap_data = copy.deepcopy(plist)
heapq.heapify(heap_data)
ck = set() # 만든 소수를 중복없이 담아 체크용으로 사용... ex. (2*2*3, 2*3*2)


ith = 0
mn = 0
while ith < N:
    mn = heapq.heappop(heap_data)
    if mn in ck:
        continue
    ck.add(mn)
    ith += 1
    for i in plist:
        if mn*i < 2**31:
            heapq.heappush(heap_data, mn*i)

print(mn)

    
    
