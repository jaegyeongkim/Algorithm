import sys
sys.stdin = open('특이한 자석.txt')
import copy
def rotation(num, k):
    new_arr = copy.deepcopy((arr))

    # print(num, k)
    left = 6
    right = 2
    rotation_num = [(num, k)]
    left_num = num
    right_num = num
    left_k = k
    right_k = k
    while left_num > 0:
        current_num = left_num
        left_num -= 1
        if arr[current_num][left] != arr[left_num][right]:
            left_k = -left_k
            rotation_num.append([left_num, left_k])
        else:
            while left_num > 0:
                rotation_num.append([left_num, 0])
                left_num -= 1
            break

    while right_num < 4:
        current_num = right_num
        right_num += 1
        if arr[current_num][right] != arr[right_num][left]:
            right_k = -right_k
            rotation_num.append([right_num, right_k])
        else:
            while right_num < 4:
                rotation_num.append([right_num, 0])
                right_num +=1
            break

    for num, k in rotation_num:
        if k == 1:
            for i in range(8):
                if i == 7:
                    arr[num][0] = new_arr[num][7]
                else:
                    arr[num][i+1] = new_arr[num][i]
        elif k == -1:
            for i in range(8):
                arr[num][i-1] = new_arr[num][i]
        elif k == 0:
            arr[num] = new_arr[num]



T = int(input())

for t in range(1, T+1):
    K = int(input())
    arr = [[0]*8]
    arr += list(list(map(int, input().split())) for _ in range(4))
    arr += [[0]*8]
    turn = list(list(map(int, input().split())) for _ in range(K))


    # 1: 시계 / -1: 반시계
    # 맞닿아 있는 곳 / 각 index의 왼쪽: 6, 오른쪽: 2
    # for row in arr:
    #     print(row)
    # print()
    # print(turn)
    for num, k in turn:
        rotation(num, k)
        # for row in arr:
        #     print(row)
        # print()
    total = 0
    for i in range(1, 5):
        total += arr[i][0]*(2**(i-1))
    print('#%d'%t, total)