lst = list(map(int, input().split()))
st = set(lst)

result = 0
if len(st) == 1:
    result = 10000 + lst[0] * 1000
elif len(st) == 2:
    lst.sort()
    result = 1000 + lst[1] * 100

else:
    result = max(lst) * 100

print(result)
