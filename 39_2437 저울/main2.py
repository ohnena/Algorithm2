# 틀렸다....


# 1 1 2 3 6 7 30

# [1] > 1
# [1,1] > 1, (1+1)
# [1,1,2] > 1, 2, (1+2), (2+2) 
# [1,1,2,3] > 1, 2, 3, 4, (1+3), (2+3), (3+3), (4+3)
# ....



N = int(input())
lst = list(map(int, input().split()))
lst.sort()


checkNum = 1
prev = lst[0]
if checkNum != prev:
    print(1)
    exit()


for i in range(1, len(lst)):
    # print("=====", prev)
    # if lst[i] >= prev + 1:
    #     print(prev+1)
    #     exit()
    for j in range(prev+1):
        if j+lst[i] <= prev:
            continue
        checkNum += 1
        if j + lst[i] != checkNum:
            break # 발견!
        # print(j,lst[i],'>',j+lst[i])
    prev = checkNum

print(checkNum)


