#백준 9375번
#패션왕 신해빈

t = int(input())
c_dict = dict()

cnt = 1

for _ in range(t):
    for _ in range(int(input())):
        c, t = input().split()
        if t in c_dict:
            c_dict[t] += 1
        else:
            c_dict[t] = 1

    for key in c_dict:
        cnt *= c_dict.get(key) + 1

    print(cnt - 1)

    c_dict.clear()
    cnt = 1
