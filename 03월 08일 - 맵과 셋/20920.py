#백준 20920번
#영단어 암기는 괴로워

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = dict()

for _ in range(n):
    w = input().rstrip()    #개행문자 제거
    if len(w) >= m:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

# 우선순위 : value값 내림차순, key의 길이가 짧은 순, key의 사전순
words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x))

for i in range(len(words)):
    print(words[i][0])      #key만 출력