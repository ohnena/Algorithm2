
N = input()
length = len(N)
N = int(N)
if N <= 10:
    print(1)
    exit()


# 0~10 >> 1
# 11~110 >> 2
# 111~1110 >> 3
# 1111~11110 >> 4

# 규칙발견...
# 2자리 // 11 결과가 1보다 작으면, 자리수 -1 프린트
# 3자리 // 111 결과가 1보다 작으면, 자리수 -1 프린트 
# N자리 // 1...1 결과가 1보다 작으면, 자리수 -1 프린트 

# 제수 구하기
tip = 0
for i in range(length):
    tip = tip*10 + 1
# 나누기
mokc = N // tip 

# 몫 비교해서 결과 출력 
if mokc < 1:
    print(length - 1)
else:
    print(length)







