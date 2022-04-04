# 백준 2503번
# 숫자 야구

import itertools

num = [str(i) for i in range(1, 10)]
nPr = list(map(''.join, itertools.permutations(num, 3)))


n = int(input())
remove_set = set()

for _ in range(n):
    
    ans, s, b = map(int, input().split())
    ans = str(ans)

    for npr in nPr:
        cnt_s = cnt_b = 0
        
        for i in range(3):
            if ans[i] == npr[i]:
                cnt_s += 1
            elif ans[i] in npr:
                cnt_b += 1

        if s != cnt_s or b != cnt_b:
            remove_set.add(npr)

nPr = [i for i in nPr if i not in remove_set]

print(len(nPr))
