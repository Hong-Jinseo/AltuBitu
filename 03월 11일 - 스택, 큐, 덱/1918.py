#백준 1918번
#후위표기식

import sys
input = sys.stdin.readline

def check_stack(st, oper):
    # top의 우선순위 >= oper의 우선순위
    while st and operator[st[-1]] >= operator(oper):
        result += st.pop()
    st.append(oper)


infix = input().rstrip()
stack = list()

operator = {'+':1, '-':1, '*':2, '/':2}   #연산자 우선순위
result = ''


for i in infix:

    # i : 연산자
    if i in operator:
        # 스택이 비었으면 스택에 넣기
        if not stack:
            stack.append(i)
        else:
            # i의 우선순위가 높으면
            if stack[-1]=='(' or operator[stack[-1]] < operator[i] :
                stack.append(i)
                
            # top의 우선순위가 높으면
            else:
                while stack and stack[-1]!='(' and operator[stack[-1]] >= operator[i]:
                    result += stack.pop()
                stack.append(i)
                
    elif i == '(':
        stack.append(i)

    elif i == ')':
        while stack and stack[-1] != '(':   # 스택의 top이 열린 괄호일 때까지 반복
            result += stack.pop()
        if stack: stack.pop()               # 스택 top(열린 괄호) 삭제

    # i : 알파벳
    else:
        result += i

# 스택에 남아있는 값이 있으면 result에 이어 붙임
for _ in range(len(stack)):
    result += stack.pop()

if '(' in result:
    result = 0

print(result)
