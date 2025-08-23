import sys
sys.stdin = open('8일차 - 암호문3.txt')

T = 2

for t in range(1, T+1):
    N = int(input())
    password = list(map(int, input().split()))
    M = int(input())
    order = list(map(str, input().split()))
    index = 0
    cnt = 0
    while cnt <= M:
        cnt += 1
        if order[index] == "I":
            for i in range(int(order[index+2]), -1, -1):
                
                password.insert(i+int(order[index+1])+1, int(order[index+3+i]))
            index += int(order[index+2])+3

        elif order[index] == "D":
            for i in range(int(order[index+2])):
                password.pop(int(order[index+1]))
            index += int(order[index+2])+2

        elif order[index] == "A":
            for i in range(int(order[index+1])):
                password.append(int(order[index+2+i]))
            index += int(order[index+1])+2
        # print(password)
    print('#%d'%t, end=' ')
    for i in range(10):
        if i == 9:
            print(password[i])
        else:
            print(password[i],end=' ')