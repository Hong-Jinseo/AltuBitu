#백준 2504번
#괄호의 값

import sys
input = sys.stdin.readline

# 올바른 괄호열인지 확인하는 함수
def is_balanced(brac):
    st = list()
    m = {']':'[', ')':'('}
    
    for i in brac:
        if i == '(' or i == '[':
            st.append(i)
        elif i == ')' or i == ']':
            if not st or st[-1] != m[i]:
                return False
            st.pop()
        else:
            print(0)
            exit()
    return not st

# 열린 괄호면 true, 닫힌 괄호면 false 반환
def is_open(brac):
    if brac == '(' or brac == '[':
        return True
    else:
        return False


bracket = input().strip()
stack = list()
temp = 0

dic = {')':2, ']':3}            # 각 괄호의 값

# 올바른 괄호열인지 확인
if not is_balanced(bracket):
    print(0)
    exit()


for brac in bracket:
    if is_open(brac):           # 열린 괄호일 경우
        stack.append(brac)      # 스택에 삽입

    # 닫힌 괄호일 경우
    else:
        if brac==')': num = 2
        elif brac==']': num = 3

        # stack의 top이 열린 괄호라면 -> 열린괄호 빼고 num값 넣어줌
        if is_open(stack[-1]):
            stack[-1] = num

        # stack의 top이 숫자라면
        else:
            while stack:
                if is_open(stack[-1]):      # top이 열린 괄호라면
                    stack[-1] = temp * num  # top = 숫자들의 합 * num
                    break
                else:
                    temp += stack[-1]       # 닫힌 괄호라면 -> temp에 더해주고
                    stack.pop()             # top값은 pop함
            temp = 0    

print(sum(stack))
