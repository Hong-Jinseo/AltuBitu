#백준 2108번
#통계학

import sys
input = sys.stdin.readline

n = int(input())
number = [int(input()) for _ in range(n)]


## 산술평균 #@
total = 0
for i in range(n): total += number[i]
print(round(total/n))


## 중앙값 ##
number.sort()
mid = int(len(number)/2)
print(number[mid])


## 최빈값 ##
dic = dict()

for i in number:
    if i in dic: dic[i] += 1
    else: dic[i] = 1

# 정렬 1순위 : 가장 많이 입력된 순서, 2순위 : 오름차순
dic = sorted(dic.items(), key= lambda x: (-x[1], x))

# 첫번째와 두번째 숫자의 빈도가 다를 경우
if len(dic)==1 or dic[0][1]!=dic[1][1]:
    print(dic[0][0])
else:
    print(dic[1][0])


## 범위 ##
print(number[len(number)-1] - number[0])
