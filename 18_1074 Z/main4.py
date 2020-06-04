

def Z(size, x, y):
    if size == 1:
        return 0  # 0??
    size //= 2

    for i in range(2):
        for j in range(2):
            # 어느 사분면에 존재하는지...
            if x < (i + 1) * size and y < (j + 1) * size:
                #
                # 구조 간소화...
                #
                before = (i * 2 + j) * (size * size) # 이전 방문 내역을 한꺼번에 계산...
                # print(i,j,"사분면 Before=",before)
                return before + Z(size, x - i * size, y - j * size) #사분면을 새로운 하나의 격자로 하여 재귀접근...
 
N, r, c = map(int, input().split())
print(Z(2**N, r, c))




# 소회
# :
# 드디어 풀이를 이해했다. 
# 이 문제는 구조화를 연습하는 문제인듯하다. 

# 1. Z함수에, 먼저 격자(2차원배열)의 사이즈 size와 방문하는 인덱스(r,c)가 주어진다. (Z(size,r,c))
# 2. 주어진 size와 (r,c)를 이용하여, r,c가 전체격자의 네개의 사분면중 X사분면에 위치하는지 알아낸다. 
# 3.1. 먼저 1 ~ X-1 사분면은 이미 방문했다 가정하고 통으로 계산. (계산값이 before변수에.)
# 3.2. X사분면을 새로운 하나의 격자로 생각하여 Z함수를 재귀적으로 다시 접근한다. (Z(size/2,new_r,new_c))
# 4. 3.1과 3.2의 합을 리턴

# 이는, 주어지는 격자가 2^N X 2^N이기때문에 가능하다.

# 위의 과정중 2.3.의 과정에서 짜실한 인덱스처리부분이 까다롭다. 그부분을 주의해서 코딩하자.


