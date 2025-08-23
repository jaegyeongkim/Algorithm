import sys
sys.stdin = open('특이한 자석.txt')

def rotation(num, k):
    new_arr = [[0]*8 for _ in range(6)]

    if k == 1:
        for i in range(8):
            if i == 7:
                new_arr[num][0] = arr[num][7]
            else:
                new_arr[num][i+1] = arr[num][i]
    else:
        for i in range(8):
            new_arr[num][i-1] = arr[num][i]

    for row in new_arr:
        print(row)
    print()

    left = 6
    right = 2
    num_left = num
    num_rigth = num
    # while num_left > 0:
    #     current_num = num_left
    #     num_left -= 1
    #     print(current_num, num_left)
    #     if arr[current_num][left] != arr[num_left][right]:
    #         for i in range(8):
    #             new_arr[num_left][i - 1] = arr[num_left][i]
    #     else:
    #         while num_left < 5:
    #             for i in range(8):
    #                 new_arr[num_left][i] = arr[num_left][i]
    #             num_left -= 1
    #         break
    while num_rigth < 5:
        current_num = num_rigth
        num_rigth += 1
        print(current_num, num_rigth)
        if arr[current_num][right] != arr[num_rigth][left]:
            for i in range(8):
                new_arr[num_rigth][i-1] = arr[num_rigth][i]
        else:
            while num_rigth < 5:
                for i in range(8):
                    new_arr[num_rigth][i] = arr[num_rigth][i]
                num_rigth += 1
            break
    for row in new_arr:
        print(row)
    print()
T = int(input())

for t in range(1, T+1):
    K = int(input())
    arr = [[0]*8]
    arr += list(list(map(int, input().split())) for _ in range(4))
    arr += [[0]*8]
    turn = list(list(map(int, input().split())) for _ in range(K))

    for row in arr:
        print(row)
    print()
    # 1: 시계 / -1: 반시계
    # 맞닿아 있는 곳 / 각 index의 왼쪽: 6, 오른쪽: 2
    cnt = 0
    for num, k in turn:
        cnt += 1
        print(cnt)
        rotation(num, k)