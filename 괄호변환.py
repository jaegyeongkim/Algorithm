import sys
sys.stdin = open('괄호변환.txt')


def solution(p):
    if p == '': return ''
    u, v = '', ''
    is_u_correct = True
    cnt = 0

    for i in range(len(p)):
        if p[i] == '(': cnt += 1
        elif p[i] == ')': cnt -= 1
        u += p[i]
        if cnt == 0:
            v = p[i+1:]
            break

    is_u_correct = check(u)
    answer = ''

    if is_u_correct:
        return u + solution(v)
    else:
        stack = ''
        v = solution(v)
        for val in u[1:-1]:
            if val == '(':
                stack += ')'
            else:
                stack += '('
        u = '(' + v + ')' + stack
        return u

def check(p):
    stack = ''
    for i in range(len(p)):
        if p[i] =='(':
            stack += p[i]
        else:
            stack = stack[:-1]
    if stack: return False
    else: return True



T = int(input())


for t in range(1, T+1):
    origin = input()
    print('#%d'%t, solution(origin))
