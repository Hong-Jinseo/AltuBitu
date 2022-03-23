# 백준 2798번
# 블랙잭

import itertools

n, m = map(int, input().split())
num = list(map(str, input().split()))

nPr = list(itertools.permutations(num, 3))
li = list()

for npr in nPr[::-1]:
    npr = list(map(int, npr))
    sum_npr = npr[0] + npr[1] + npr[2]
    
    sum_npr = sum(npr)
    if sum_npr <= m:
        li.append(sum_npr)

li.sort()
print(li[-1])
