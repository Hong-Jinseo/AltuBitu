#백준 19583번
#싸이버개강총회

import sys
input = sys.stdin.readline

def time_to_int(time_str):
    time_int = int(time_str[:2]+time_str[3:])
    return time_int


s, e, q = input().split()
s = time_to_int(s)
e = time_to_int(e)
q = time_to_int(q)

before = set()
after = set()


'''
while True:
    data = input()
    if len(data)<5:
        print(len(data))
        break
'''

line = sys.stdin.readlines()
for data in line:
    time, name = data.split()
    time = time_to_int(time)

    if time<=s:
        before.add(name)
    elif e<=time<=q:
        after.add(name)

count = 0
for i in before:
    if i in after:
        count += 1
print(count)