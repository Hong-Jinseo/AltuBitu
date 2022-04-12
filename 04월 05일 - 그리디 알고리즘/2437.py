# 백준 2437번
# 저울

import sys                      # sys 모듈 import
input = sys.stdin.readline      # 내장함수 input 대신 sys 모듈의 stdin.readline 사용

"""
[저울]
- 작은 값부터 측정 가능한지 파악해야 하므로, 오름차순으로 정렬한다.
- 현재 0부터 scope까지 모든 무게를 빠짐없이 측정가능하다고 했을 때, 새로운 무게는 scope + 1보다 작거나 같아야 한다.
- ex) 현재 1~5까지 측정 가능한데, 다음 값이 7인 경우 -> 6은 측정 불가
- 만약 이 조건을 만족할 경우, 측정 가능한 범위는 [1, scope + 새로운 무게]로 갱신된다.
- 모든 저울을 살펴봤는데도 비어있는 값이 없으면, scope + 1 리턴
"""

def find_unmeasurable(weight):  # 측정 불가능한 값을 리턴하는 함수
    weight.sort()               # 작은 무게부터 봐야 하므로 정렬
    scope = 0                   # 측정 가능 범위값

    for w in weight:            # 무게추 리스트에 순차적으로 접근
        if scope + 1 < w:       # 새로운 무게가 scope + 1보다 크다면
            return scope + 1    # scope+1 반환
        scope += w              # 새로운 무게가 scope + 1보다 작거나 같다면 -> 측정 가능 범위가 scope + 새로운 무게까지로 갱신됨

    return scope + 1            # 1부터 scope까지 비어있는 값이 없다면 -> scope+1 반환

n = int(input())                # n = 저울추의 개수
weight = list(map(int, input().split()))    # weight = [저울추의 무게를 나타내는 n개의 양의 정수]

print(find_unmeasurable(weight))            # 함수 find_unmeasurable의 return값을 출력