N, target = int(input()), list(map(int, input().split()))
M, nums = int(input()), list(map(int, input().split()))

d = dict()
for n in nums:
    d[n] = 0

for i in target:
    if i in d.keys():
        d[i] = 1

for n in nums:
    print(d[n])
