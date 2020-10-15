import sys

sys.stdin = open('사다리 조작.txt')


def check_short(comb):
    # 연결 시킴
    for i in range(len(comb)):
        arr[comb[i][0]][comb[i][1]] = comb[i][1] + 1
        arr[comb[i][0]][comb[i][1] + 1] = comb[i][1]

    result = movement()

    # 연결 해제
    for i in range(len(comb)):
        arr[comb[i][0]][comb[i][1]] = 0
        arr[comb[i][0]][comb[i][1] + 1] = 0

    return result


# 사다리 움직이는 코드
def movement():
    for c in range(1, N + 1):
        sc = c
        r = 0
        while 1:
            r += 1
            if r == H + 1:
                r -= 1
                if sc != c:
                    return 0
                break
            if arr[r][c] == 0:
                continue
            else:
                c = arr[r][c]
    return 1


T = int(input())

for t in range(1, T + 1):
    N, M, H = map(int, input().split())
    info = list(list(map(int, input().split())) for _ in range(M))
    arr = [[0] * (N + 1) for _ in range(H + 1)]

    for i in range(len(info)):
        arr[info[i][0]][info[i][1]] = info[i][1] + 1
        arr[info[i][0]][info[i][1] + 1] = info[i][1]
    result = movement()

    # 안 옮겨도 되면 출력
    if result == 1:
        print(0)

    if result == 0:
        check = []
        for i in range(1, H + 1):
            for j in range(1, N + 1):
                # 연결이 아무것도 안 되어있으면
                if arr[i][j] == 0:
                    # index가 초과되지 않으면
                    if j + 1 < N + 1:
                        # 다음 칸에 연결이 가능하면
                        if arr[i][j + 1] == 0:
                            check.append([i, j])

        # 하나로 되냐?
        for i in range(len(check)):
            # index가 초과되면 continue
            if check[i][1] >= N:
                continue
            comb = []
            comb.append(check[i])
            result = check_short(comb)
            if result == 1:
                print(1)
                break

        if result == 0:
            # 두개 연결하면 되냐?
            for i in range(len(check)):
                # index가 초과되면 break
                if i + 1 >= len(check):
                    break
                # index가 초과되면 continue
                if check[i][1] >= N:
                    continue
                for j in range(i + 1, len(check)):
                    # index가 초과되면 continue
                    if check[j][1] >= N:
                        continue
                    comb = []
                    comb.append(check[i])
                    comb.append(check[j])
                    result = check_short(comb)
                    if result == 1:
                        print(2)
                        break
                if result == 1:
                    break

            if result == 0:
                # 세개 연결하면 되냐?
                for i in range(len(check)):
                    # index가 초과되면 break
                    if i + 1 >= len(check):
                        break
                    # index가 초과되면 continue
                    if check[i][1] >= N:
                        continue
                    for j in range(i + 1, len(check)):
                        # index가 초과되면 break
                        if j + 1 >= len(check):
                            break
                        # index가 초과되면 continue
                        if check[j][1] >= N:
                            continue
                        for k in range(j + 1, len(check)):
                            # index가 초과되면 continue
                            if check[k][1] >= N:
                                continue
                            comb = []
                            comb.append(check[i])
                            comb.append(check[j])
                            comb.append(check[k])
                            result = check_short(comb)
                            if result == 1:
                                print(3)
                                break
                        if result == 1:
                            break
                    if result == 1:
                        break

                if result == 0:
                    # -1 출력
                    print(-1)
