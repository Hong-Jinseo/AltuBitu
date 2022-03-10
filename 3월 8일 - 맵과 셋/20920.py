#백준 20920번
#영단어 암기는 괴로워

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = dict()

for _ in range(n):
    w = input().rstrip()
    if len(w) >= m:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x))

for i in range(len(words)):
    print(words[i][0])
