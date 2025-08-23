import sys
sys.stdin = open('연산자 끼워넣기.txt')
def permutation(idx):
    if idx == N-1:
        calculation(copy)
        return
    else:
        for i in range(N-1):
            if selected[i] == 0:
                selected[i] = 1
                copy[idx] = act_list[i]
                permutation(idx+1)
                selected[i] = 0

def calculation(copy):
    global min_cal, max_cal
    result = arr[0]

    for i in range(len(arr)-1):
        if copy[i] == 0:
            result += arr[i+1]
        elif copy[i] == 1:
            result -= arr[i+1]
        elif copy[i] == 2:
            result *= arr[i+1]
        elif copy[i] == 3:
            if result < 0:
                result = -result
                result = -(result // arr[i+1])
            else:
                result = result // arr[i+1]

    if max_cal < result:
        max_cal = result
    if min_cal > result:
        min_cal = result


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    act = list(map(int, input().split()))
    act_list = []
    min_cal = 1000000000
    max_cal = -1000000000
    for i in range(4):
        for j in range(act[i]):
            act_list.append(i)

    selected = [0] * (N-1)
    copy = [0] * (N-1)


    permutation(0)
    print(max_cal)
    print(min_cal)