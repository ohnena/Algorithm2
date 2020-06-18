
# 소수체크
import math
def isPrime(N):
    for i in range(2, N):
        if N % i == 0:
            return False
        # if i >= math.sqrt(N):  # 시간 복잡도를 O(N) > O(루트N)
        if i*i > N:
            break
    return True

assert isPrime(331)
assert isPrime(19)
    

# 소인수분해 (조금 까다롭..)
def prime_factorization(N):
    p, fac = 2, []
    # while p < math.sqrt(N): # 시간 복잡도를 O(N) > O(루트N)
    while p**2 <= N:
        if N%p == 0:
            N //= p
            fac.append(p)
        else:
            p += 1
    if N > 1:
        fac.append(N)
    return fac 

print(prime_factorization(12345))
print(prime_factorization(16))

    



# 실전 코테에서는 소수리스트를 미리 만들어놓아야 하는 경우가 있다
# 이때 만약 위의 isPrime(N)을 이용한다면, O(N*루트N)이 되므로 
# 안전한 선택지가 아니다. 
# 이때, 에라토스테네스의 체를 이용하자. O(N*로그로그N)이기때문이다!



def getPrimeList(N): # N보다 작은 소수리스트 구하기
    A, plist = [0 for _ in range(N+1)], []
    for i in range(2, N):
        if A[i] == 0: # 소수인 경우...
            plist.append(i)
        else:
            continue
        for j in range(i*2, N, i):
            A[j] = 1
    return plist



print(getPrimeList(100))


def prime_factorization_2(N, p): # 에라토스테네스의 체 원리를 사용...
    fac = []
    for i in p:
        if N==1 or N < i*i : 
            break 
        while N%i == 0:
            fac.append(i)
            N //= i
    if N > 1:
        fac.append(N)
    return fac 


assert prime_factorization_2(12345, getPrimeList(12345)) == prime_factorization(12345)
assert prime_factorization(16) == prime_factorization_2(16, getPrimeList(16))

print("========")
print(prime_factorization(12345))
print(prime_factorization_2(12345, getPrimeList(12345)))
print(prime_factorization(16))
print(prime_factorization_2(16, getPrimeList(16)))




# 활용 3종
# 1 소인수의 개수
def era_factor_count(N): # O(NlogN) 정도...
    A = [0 for _ in range(N+1)]
    for i in range(2, N): # 해답에는 2가 아닌 1로 되어있네?...
        for j in range(i, N, i):
            A[j] += 1  # 배수가 존재한다면 +1
    return A
# 2 소인수의 합
def era_factor_sum(N):
    A = [0 for _ in range(N+1)]
    for i in range(2, N): 
        for j in range(i, N, i):
            A[j] += i  # 배수가 존재한다면 +1
    return A
# 3 소인수분해
def era_factorization(N):
    A = [0 for _ in range(N+1)]
    for i in range(2, N): 
        if A[i] : continue
        for j in range(i, N, i):
            A[j] = i  # 결국 A[x]에는 x의 가장큰 소인수가 저장되어 있겠다.
    return A


print(era_factor_count(7))
print(era_factor_sum(7))
print(era_factorization(100))



# 예) 에라토스테네스의 체를 이용한 소인수 분해 방법...
# A[x] = x의 가장 큰 소인수
A = era_factorization(100)
N = 84
while A[N] != 0:
    print(A[N])
    N //= A[N]