# *3개 함수 구현
# rotate90(B,N) 
#     return NB
# convert(lst, N) 
#     return new_list + [0]*(N-len(new_list))
# bfs(N, B, count)
#     return ret
# print(dfs(N,Board,5))

# *주의!) 되도록 전역변수 사용안하고 풀어보도록 하자!

# *팁) 함수들로 쪼개서 풀되, 함수 내부가 20줄이 넘어가지 않도록 하자!



# 00 01 02
# 10 11 12
# 20 21 22
# >
# 20>00 10>01 00>02
# 21>10 11>11 01>12
# 22>20 12>21 02>22

# abs(j-(size-1)),i> i,j



# 해답기반...

N = int(input())
Board = []
for _ in range(N):
    row = list(map(int, input().split()))
    Board.append(row)



def rotate90(size, board):
    nboard = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            nboard[j][(size-1)-i] = board[i][j]            
            # nboard[i][j] = board[abs(j-(size-1))][i] 틀렸다...
    return nboard



def convert(size, lst):

    new_lst = [i for i in lst if i != 0] # move
    for i in range(len(new_lst)-1):      # crush
        if new_lst[i] == new_lst[i+1]:
            new_lst[i] += new_lst[i+1]
            new_lst[i+1] = 0       
    new_lst = [i for i in new_lst if i != 0] # move
    
    return new_lst + [0] * (size-len(new_lst))



def _debugPrint(size, board):
    print("================")
    for i in range(size):
        for j in range(size):
            print(board[i][j], end=' ')
        print()



def dfs(size, board, count):

    ret = max([max(row) for row in board])
    if count == 0:
        return ret
    for _ in range(4):
        nboard = [convert(size,row) for row in board]
        if nboard != board:
            ret = max(ret, dfs(size, nboard, count-1))
        board = rotate90(size, board)
    
    return ret


    


print(dfs(N,Board,5))
