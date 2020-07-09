import sys
sys.stdin = open('괄호변환.txt')


'''
문제를 이해하는데 1시간 걸린 것 같다.
3시간 풀고 안 맞아서 다른 사람 풀이를 봤는데 문제 자체를 잘못 이해해서 틀린 거였다.
그리고 뒤집는다는 부분에서도 잘못 이해해서 한참 걸렸다.


문제를 잘 이해하는 능력과 천천히 다시 하나씩 보는 능력을 길러보자 재경아
'''


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
