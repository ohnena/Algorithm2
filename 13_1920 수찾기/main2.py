N, target = int(input()), {i:1 for i in map(int, input().split())}
M = int(input())

for i in list(map(int, input().split())):
    print(target.get(i, 0)) # 딕셔너리의 get메소드 사용...