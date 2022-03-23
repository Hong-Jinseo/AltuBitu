# 백준 2858번
# 기숙사 바닥

r, b = map(int, input().split())

# L + W = R/2 + 2
# L * W = R + B
lw_add = r/2 + 2
lw_mul = r + b

l = w = 0

for i in range(3, 5000):
    for j in range(3, 5000):
        if i + j == lw_add and i * j == lw_mul:
            l, w = i, j
            break
    if l != 0 and w != 0:
        break

if l < w:
    print(w, l)
else:
    print(l, w)
