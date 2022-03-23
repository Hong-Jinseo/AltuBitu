# 백준 10610번
# 30

n = list(input())
n.sort(reverse=True)

total = 0

if '0' in n:
    for i in n:
        total += int(i)
    if total % 3 == 0:
        print("".join(n))
    else:
        print(-1)
else:
    print(-1)
