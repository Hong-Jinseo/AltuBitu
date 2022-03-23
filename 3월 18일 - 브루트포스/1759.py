# 백준 1759번
# 암호 만들기

import itertools
import sys
input = sys.stdin.readline


vowels = ['a', 'e', 'i', 'o', 'u']
remove_set = set()

L, C = map(int, input().split())
alphabet = list(input().split())

nPr = list(map(list, itertools.combinations(alphabet, L)))      # 튜플 -> 리스트

# 암호 내 알파벳 정렬
for i in range(len(nPr)):
    nPr[i].sort()

# 중복되는 암호 삭제
nPr = list(set(map(tuple, nPr)))

# 최소 한 개의 모음, 최소 두 개의 자음
for npr in nPr:
    v_cnt = c_cnt = 0
    for k in range(L):
        if npr[k] in vowels:
            v_cnt += 1
        else:
            c_cnt += 1
    if v_cnt < 1 or c_cnt < 2:
        remove_set.add(npr)

nPr = [i for i in nPr if i not in remove_set]

# 암호 전체 정렬 
nPr.sort()

for data in nPr:
    print(''.join(data))
