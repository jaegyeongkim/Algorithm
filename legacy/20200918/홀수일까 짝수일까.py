import sys
sys.stdin = open('홀수일까 짝수일까.txt')

T = int(input())

for t in range(1, T+1):
    num = int(input())
    if num % 2:
        result = 'Odd'
    else:
        result = 'Even'
    print('#%d'%t, result)