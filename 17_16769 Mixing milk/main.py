capacity=[0]*3
amount=[0]*3

for i in range(3):
    capacity[i], amount[i] = map(int, input().split())

for i in range(100):
    cdx = i % 3         # current_index
    ndx = (i+1) % 3     # next_index
    
    # moved = min(capacity[ndx] - amount[ndx], amount[cdx])
    # amount[cdx] -= moved
    # amount[ndx] += moved 
    
    # 위처럼 변수 moved 사용하지 않고...
    # 다만 주의, 같은 라인에 표시된건, 우측 항이 한꺼번에 계산된다.
    amount[cdx],amount[ndx] = max(amount[cdx]-(capacity[ndx]-amount[ndx]),0),min(capacity[ndx], amount[ndx]+amount[cdx])


for i in range(3):
    print(amount[i])


# 10 3
# 11 4
# 12 5