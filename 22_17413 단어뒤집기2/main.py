# 첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.

# 출력
# 첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.


# *구상...
# 순회하면서 검사
#     태그시작시, 태그종료까지 그대로 패스 (flag사용)
#     flag=False인상태에서 만난 공백아닌 문자라면, 다음 태그 혹은 공백전까 stack.push. 태그 공백 만나면, 전부 pop 

# 케이스 분석
# for문으로 문자열순회
#     태그상태True,
#         그냥출력
#         태그종료문자(>)이면, 태그상태=False
        
#     태그상태False,
#         if 태그시작문자(<)이면, 스택팝 출력 + <출력 + 태그상태=True
#         elif 공백이면 스택팝 출력 + 공백출력
#         else(문자면) 스택푸시
# for문 종료후, 스택팝 출력 후 프로그램종료


def printStack(stack):
    if len(stack) > 0:
        while stack:  
            print(stack.pop(), end='')

S = str(input())
isTag = False
stack = []
for c in S:
    # c = S[i]
    if isTag:
        print(c, end='')
        if c == '>':
            isTag = False
    else:
        if c == '<':
            printStack(stack)
            print('<', end='')
            isTag = True
        elif c == ' ':
            printStack(stack)
            print(' ', end='') 
        else:
            stack.append(c)
printStack(stack)













def checkString(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

# for _ in range(1):#int(input()))
S = input()

stack = []
isTag = True
for c in S:
    if isTag:
        # print(c, end='')
        result.append(c)
        continue
    if c == '<':
        printStack(stack)
        isTag = True
        # print(c, end='')
        result.append(c)
        continue
    if c == '>':
        # print(c, end='')
        result.append(c)
        isTag = False
        continue


    if not isTag and c != ' ':
        stack.append(c, end='')
        continue
    if c == ' ':
        printStack(stack)
        # print(c, end='')
        result.append(c)
        continue
    
print(''.join(result))
print(checkString(S, ''.join(result)))
# assert ''.join(result) is S

    

    


    

    

    

# 예제 입력 1  복사
# baekjoon online judge
# 예제 출력 1  복사
# noojkeab enilno egduj
# 예제 입력 2  복사
# <open>tag<close>
# 예제 출력 2  복사
# <open>gat<close>
# 예제 입력 3  복사
# <ab cd>ef gh<ij kl>
# 예제 출력 3  복사
# <ab cd>fe hg<ij kl>
# 예제 입력 4  복사
# one1 two2 three3 4fourr 5five 6six
# 예제 출력 4  복사
# 1eno 2owt 3eerht rruof4 evif5 xis6
# 예제 입력 5  복사
# <int><max>2147483647<long long><max>9223372036854775807
# 예제 출력 5  복사
# <int><max>7463847412<long long><max>7085774586302733229
# 예제 입력 6  복사
# <problem>17413<is hardest>problem ever<end>
# 예제 출력 6  복사
# <problem>31471<is hardest>melborp reve<end>
# 예제 입력 7  복사
# <   space   >space space space<    spa   c e>
# 예제 출력 7  복사
# <   space   >ecaps ecaps ecaps<    spa   c e>