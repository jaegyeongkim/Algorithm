'''
알고리즘이 계속 헷갈려서 오래걸렸다. 한 2시간 30분 걸린듯
처음에는 반대로 마지막 거만 구하면 되는줄 알았는데 반례가 있어서 70점 나왔다
그래서 처음부터 다시 품
오래 걸릴 문제가 아닌데 범위에서 index out of range 떠서 빡이 많이 침
'''
def solution(n, t, m, timetable):
    array = []
    for time in timetable:
        # print(time)
        Hour, Min = map(int, time.split(':'))
        array.append(Hour * 60 + Min)

    array.sort()

    crew_bus = [[] for _ in range(n)]
    # print(array)

    total_cnt = 0
    for n in range(n):
        const_bus = 9*60 + n*t
        crew_bus[n].append(const_bus)
        cnt = 0
        while 1:
            cnt += 1
            if array[0] <= const_bus:
                crew_bus[n].append(array.pop(0))
            if cnt == m or len(array) == 0:
                break
    # print(crew_bus)
    # print(crew_bus[-1])
    if len(crew_bus[-1]) == m+1:
        answer = crew_bus[-1][m]-1
    else:
        answer = crew_bus[-1][0]

    Hour = str(answer // 60)
    Min = str(answer % 60)
    if len(Hour) == 1:
        Hour = '0' + Hour
    if len(Min) == 1:
        Min = '0' + Min
    answer = Hour + ':' + Min
    # print(answer)
    return answer