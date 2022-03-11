#백준 19583번
#싸이버개강총회

import sys
input = sys.stdin.readline

# hh:mm 형식의 시간을 4자리 int형으로 변환
def time_to_int(time_str):
    time_int = int(time_str[:2]+time_str[3:])
    return time_int


s, e, q = input().split()
s = time_to_int(s)
e = time_to_int(e)
q = time_to_int(q)

before = set()      #개강총회 시작 전 채팅한 사람 목록
after = set()       #개강총회 종료 후 채팅한 사람 목록

'''
while True:
    data = input()  
    if len(data)<4: #입력값의 길이가 5 미만이라면 (hh:mm이 입력되지 않은 경우)
        break
'''

line = sys.stdin.readlines()    #파일 전체 내용을 가져와 리스트로 반환
for data in line:               #리스트 값을 하나씩 data가 가져옴
    time, name = data.split()   
    time = time_to_int(time)

    if time<=s:
        before.add(name)
    elif e<=time<=q:
        after.add(name)

count = 0
for i in before:        #before에 있는 이름이
    if i in after:      #after에도 있다면
        count += 1      #count에 1 추가
print(count)