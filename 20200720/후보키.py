def powerset(N, idx, arr, selected, copy):
    global cnt
    if idx == N:
        for i in range(N):
            if selected[i] == 1:
                copy[cnt].append(arr[i])
        cnt += 1
        return copy

    selected[idx] = 1
    powerset(N, idx + 1, arr, selected, copy)
    selected[idx] = 0
    powerset(N, idx + 1, arr, selected, copy)
    return copy


def possible(minimality, copy):
    for m in range(len(minimality)):
        cnt = 0
        for n in minimality[m]:
            for l in copy:
                if n == l:
                    cnt += 1
                    break
        if cnt == len(minimality[m]):
            return 0
    return 1


def solution(relation):
    # 부분집합 리스트 구하기
    N = len(relation[0])
    selected = [0] * N
    copy = [[] for _ in range(2 ** N)]
    arr = list(range(N))
    copy = powerset(N, 0, arr, selected, copy)
    copy.sort(key=lambda x: len(x))

    minimality = []
    for i in range(len(copy)):
        is_possible = True

        if len(copy[i]) == 0:
            continue

        if len(minimality) > 0:
            is_possible = possible(minimality, copy[i])

        list_up = [[] for _ in range(len(relation))]

        for j in range(len(relation)):
            for k in copy[i]:
                list_up[j].append(relation[j][k])
            for l in range(j):
                if list_up[l] == list_up[j]:
                    is_possible = False
            if is_possible == False:
                break
        if is_possible == False:
            continue

        minimality.append(copy[i])

    answer = len(minimality)

    return answer


cnt = 0