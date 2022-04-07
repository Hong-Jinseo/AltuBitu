# 백준 5397번
# 키로거

t = int(input())

for _ in range(t):
    pw = input()

    left, right = [], []    # 커서를 기준으로 좌우

    for key in pw:
        if key == '<':
            if left:
                right.append(left.pop())

        elif key == '>':
            if right:
                left.append(right.pop())

        elif key == '-':
            if left:
                left.pop()
                
        else:
            left.append(key)

    print(''.join(left) + ''.join(right[::-1]))
