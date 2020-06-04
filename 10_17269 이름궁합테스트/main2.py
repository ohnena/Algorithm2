# 해답...
L1, L2 = map(int, input().split(' '))
A, B = map(str, input().split(' ')) 

num = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

AB = ''
min_len = min(L1,L2)
for i in range(min_len):
    AB += A[i] + B[i]

AB += A[min_len:] + B[min_len:] # 리스트 슬라이싱
lst = [num[ord(i)-ord('A')] for i in AB]

for i in range(L1+L2-2):
    for j in range(L1+L2-1-i):
        lst[j] = lst[j] + lst[j+1]

print("{}%".format(lst[0] % 10 * 10 + lst[1] % 10)) #.format이용...