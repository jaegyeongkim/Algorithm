import sys
sys.stdin = open('차량 정비소.txt')

T = int(input())

for t in range(1, T+1):
    N, M, K, A, B = map(int, input().split())   # 접수 창구 / 정비 창구 / 고객 수 / 지갑두고 간 손님 이용 창구
    A_arr = list(map(int, input().split())) # 접수 창구에서 각각 걸리는 시간
    B_arr = list(map(int, input().split())) # 정비 창구에서 각각 걸리는 시간
    visitor_time = list(map(int, input().split()))
    visitor_dic = {}

    for i in range(len(visitor_time)):
        if visitor_time[i] not in visitor_dic:
            visitor_dic[visitor_time[i]] = [i+1]
        else:
            visitor_dic[visitor_time[i]].append(i+1)
    A_station = []
    B_station = []
    A_station_dic = {}
    B_station_dic = {}
    for i in range(len(A_arr)):
        A_station.append([A_arr[i], 0, 0])  # 몇분 걸린다, 몇분 남았다, 몇번 손님이다.
        A_station_dic[i+1] = []
    for i in range(len(B_arr)):
        B_station.append([B_arr[i], 0, 0])
        B_station_dic[i+1] = []
    # print(N, M, K, A, B)
    # print(A_station)
    # print(B_station)
    # print(visitor_dic)
    time = 0
    A_wating = []
    B_wating = []
    while 1:
        for i in range(len(A_station)):
            if A_station[i][1] > 0:
                A_station[i][1] -= 1
                if A_station[i][1] == 0:
                    # A_wating[A_station[i][2]-1][1] = 1  # 몇번 손님이 제공 받았다.
                    B_wating.append([A_station[i][2], 0])   # 몇번 손님 / 제공 안 받았다.
                    A_station_dic[i+1].append(A_station[i][2])

        for i in range(len(B_station)):
            if B_station[i][1] > 0:
                B_station[i][1] -= 1
                if B_station[i][1] == 0:
                    B_station_dic[i+1].append(B_station[i][2])

        if time in visitor_dic:                 # 몇분에 A wating 손님 받는 로직
            for visitor in visitor_dic[time]:
                A_wating.append([visitor, 0])   # 몇번 손님이 / 제공 안 받았다.

        for i in range(len(A_wating)):          # A station이 비어있으면 손님을 넣어준다.
            if A_wating[i][1] == 0:
                for j in range(len(A_station)):
                    if A_station[j][1] == 0:
                        A_station[j][1] = A_station[j][0]
                        A_station[j][2] = A_wating[i][0]
                        A_wating[i][1] = 1
                        break

        for i in range(len(B_wating)):          # B station이 비어있으면 손님을 넣어준다.
            if B_wating[i][1] == 0:
                for j in range(len(B_station)):
                    if B_station[j][1] == 0:
                        B_station[j][1] = B_station[j][0]
                        B_station[j][2] = B_wating[i][0]
                        B_wating[i][1] = 1
                        break

        # print(time)
        # print(A_wating)
        # print(A_station)
        # print(B_wating)
        # print(B_station)

        time += 1
        total = 0
        for key, value in B_station_dic.items():
            total += len(value)
        if total == K:
            break

        # print(A_station_dic, B_station_dic)
    total = 0
    for i in A_station_dic[A]:
        for j in B_station_dic[B]:
            if i == j:
                total += i
    if total == 0:
        total = -1
    print('#%d'%t, total)