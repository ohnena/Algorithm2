N = input()
length = len(N)
tip = '1'*length 

if int(N) == 0:
    print(1)
    exit()
    
if int(N) < int(tip):
    print(length-1)
else:
    print(length)


# 0 1 2 3 4 5 6 7 8 9 (<11)
# 0 1 2 3 4 5 6 7 8 9 (<111)
# 0 1 2 3 4 5 6 7 8 9 (<1111)


