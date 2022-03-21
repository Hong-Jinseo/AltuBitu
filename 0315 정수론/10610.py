# 백준 10610번
# 30

n = list(input())
n.sort(reverse=True)
num = "".join(n)

if int(num)%30 != 0:
    print(-1)
else:
    print(num)
