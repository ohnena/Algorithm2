N, M = map(int, input().split())

team_mem = {}
mem_team = {}
for _ in range(N):
    team, mem_num = input(), int(input())
    team_mem[team] = []
    for i in range(mem_num):
        name = input()
        team_mem[team].append(name)
        mem_team[name] = team



for i in range(M):
    keyword, type = input(), int(input())
    if type == 0:
        #멤버이름 사전순 정렬 출력
        for name in sorted(team_mem[keyword]):
            print(name)

    else:
        #팀이름 출력
        print(mem_team[keyword])

    
