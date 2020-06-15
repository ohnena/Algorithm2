# 해답...

N = int(input())
A = list(map(int, input().split()))
A.sort() # 정렬필수 


# 1 1 2 3 6 7 30

# 1> 1까지 가능
# 1> 2까지 가능
# 2> 4까지 가능
# 3> 7까지 가능
# 6> 13까지 가능
# 7> 20까지 가능
# 30> 21 불가능... (30아닌, 커도 21은 나와줘야 연결이 가능해짐...)


prev = 0
for i in range(len(A)):
    if A[i] <= prev+1: # prev+1이 가능하려면 ...
        prev += A[i]
    else:
        break
print(prev+1)

