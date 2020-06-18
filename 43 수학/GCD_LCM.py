# 최대공약수 GCD 구하기
#1 단순하게 반복문으로
#2 유클리드 호제법(재귀)
#3 유클리드 호제법(반복문)
#4 math라이브러리.gcd(...)사용...



def gcd_naive(a, b): 
    for i in range(min(a,b),0,-1):
        if a%i == 0 and b%i == 0:
            return i

def gcd(a, b): # 재귀...
    if a%b == 0: return b
    return gcd(b, a%b)

def gcd2(a, b):
    while a%b != 0:
        a, b = b, a%b
    return b 



A,B=28,56

import math
assert gcd_naive(A,B) == math.gcd(A,B)
assert gcd(A,B) == math.gcd(A,B)
assert gcd2(A,B) == math.gcd(A,B)




# 최소공배수 LCM 구하기
# gcd를 이용하는 공식을 그대로 사용!
# 단, 주의! c, java같은 경우에는 int overflow가 발생할 수 있으니
# a / gcd(a,b) * b로 하라고!
def lcm(a, b):
    # return a*b / gcd(a,b)
    return a/gcd(a,b) * b 

