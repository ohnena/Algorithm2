L1, L2 = map(int, input().split(' '))
name1, name2 = map(str, input().split(' ')) 


def convert(c):
    num = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
    i = ord(c) - ord('A')
    return num[i]


mixed = []
max_length = max(L1, L2)
for i in range(max_length):
    if i < L1:
        mixed.append(convert(name1[i]))    
    if i < L2:
        mixed.append(convert(name2[i]))


i = len(mixed)-1

while (True):
    if i < 2:
        break
    for j in range(i):

        mixed[j] = (mixed[j] + mixed[j+1]) % 10
    mixed[i] = 'E'
    i -= 1

result = mixed[0] * 10 + mixed[1]
result = str(result) + '%'
print(result)