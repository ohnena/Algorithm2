# 2, 5, 7이었다면, 이러한 곱들을 오름차순으로 나타내 보면, 
# 2, 4, 5, 7, 8, 10, 14, 16, 20, 25, 28, 32, 35, 등이 된다.

# K개의 소수가 주어졌을 때, 이러한 소수의 곱들 중에서 N번째 수를 구해 보자. 
# 단 정답은 2^31보다 작은 자연수이다.


# 1가능? N. 1%2=1 > 1%5=1 > 1%7=1 >>> != 0 존재 X
# 2가능? Y. 2/2=1 > 몫1 발견! >> 해결! //2%2=0 >>> 0 != 0 존재 O
# 3가능? N. 3%2=1 > 3%5=3 > 3%7=3 >>> !=0 존재 X
# 4가능? Y. 4/2=2, 2/2=1 >>> 몫1 발견!>> 해결!
# 5가능? Y. 5/2!=1 >> 5/5=1 >>> 몫1 발견! >> 해결
# 6가능? N. 6/2=3 > 3/5 > 3/7 >>> 몫1 발견X 
# 7가능?

K, N = map(int, input().split())
P = list(map(int, input().split())) # 이미 오름차순...

# M을 P[i]으로 나눈다. 
#     나머지가 0이다. 
#         몫이 1이 아니다. M=몫 한 후, P[i]로 처음부터 다시...
#         몫이 1이다. 카운트++ 리턴
#     나머지가 0이아니다.
#         P[i+1]로 처음부터 다시...

def isPossible(target, primes, idx):
    if idx >= len(primes):
        return False

    ret = False
    rem = target % primes[idx]
    if rem == 0:
        por = target / primes[idx]
        if por != 1:
            ret = isPossible(por, primes, idx)
        else:
            ret = True
    else:
        ret = isPossible(target, primes, idx+1)
    
    return ret


cnt = 0
for cand in range(1, 2**31+1):
    if isPossible(cand, P, 0):
        cnt += 1
        print(cnt, cand)
        if cnt == N:
            print(cand)
            break



