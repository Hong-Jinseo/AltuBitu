# 백준 20055번
# 컨베이어 벨트 위의 로봇

from collections import deque
import sys
#sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, k = map(int, input().split())
A = deque(list(map(int, input().split())))  #내구도
robot = deque(False for _ in range(n))      #로봇
#robot = deque(0 for _ in range(n))
count = 0


while True:
    count += 1
    
    # 과정1
    A.rotate(1)
    robot.rotate(1)
    robot[-1] = False

    # 과정2
    if True in robot:
        for i in range(n-2, -1, -1):
            if robot[i] and not robot[i+1] and A[i+1]>0:
                robot[i] = False
                robot[i+1] = True
                A[i+1] -= 1
    robot[-1] = False

    # 과정3
    if A[0]>0:
        robot[0] = True
        A[0] -= 1

    # 과정4
    if A.count(False) >= k:
        break
    
print(count)
