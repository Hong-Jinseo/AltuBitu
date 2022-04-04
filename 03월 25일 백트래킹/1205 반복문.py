# 백준 1205번
# 등수 구하기

import sys
input = sys.stdin.readline


# 저장된 개수, 태수의 점수, 저장 가능 개수
n, s, p = map(int, input().split())
if n>0:
    ranking = list(map(int, input().split()))

    if n==p and ranking[-1]>=s:
        print(-1)
    else:
        for i in range(n):
            if ranking[i] <= s:
                break
            i += 1
        #이 부분을 for문-if문 안에 넣었더니 i가 p인 경우에 작동 X
        print(i+1)
else:
    print(1)
