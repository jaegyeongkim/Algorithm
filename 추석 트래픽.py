def data(lines, scope):
    arr = list(map(str, lines.split()))
    # print(arr)
    time = list(map(str, arr[1].split(':')))

    #     print(float(arr[2][:-1]))

    #     print(round(float(time[2]) - float(arr[2][:-1]) + 0.001, 3))
    Hour = float(time[0])
    Min = float(time[1])
    Sec = Hour * 3600 + Min * 60 + float(time[2])
    # scope.append([(round(Sec - float(arr[2][:-1]) + 0.001, 3))*1000, Sec*1000])
    scope.append([int((round(Sec - float(arr[2][:-1]) + 0.001, 3)) * 1000), int(Sec * 1000)])


def solution(lines):
    if len(lines) == 1:
        return 1
    scope = []
    for i in range(len(lines)):
        data(lines[i], scope)
    print(scope)
    max_cnt = 0
    for i in range(len(scope)):
        if i > 0:
            before_max = scope[i][1]
        else:
            before_max = scope[0][0]
        for j in range(scope[i][1] - before_max + 1):
            cnt = 0
            scope_left = before_max + j
            scope_right = scope_left + 999
            for k in range(len(scope)):
                if scope_left > scope[k][1]:
                    pass
                elif scope_right < scope[k][0]:
                    pass
                else:
                    cnt += 1

            if max_cnt < cnt:
                max_cnt = cnt
        # print(max_cnt)

    answer = max_cnt
    return answer