import sys
sys.stdin = open('note.txt')

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
    print(answer)
    return answer


T = int(input())

for t in range(1, T+1):
    n, t, m = map(int, input().split())
    timetable = list(input().split())

    solution(n, t, m, timetable)
    print()


'''
반대로
'''


# def solution(n, t, m, timetable):
#     array = []
#     for time in timetable:
#         # print(time)
#         Hour, Min = map(int, time.split(':'))
#         array.append(Hour * 60 + Min)
#
#     array.sort(reverse=True)
#     # print(array)
#
#     last = 9 * 60 + (n - 1) * t
#     last_crew = []
#     for crew in array:
#         if crew <= last:
#             last_crew.append(crew)
#         if len(last_crew) == m:
#             break
#     # print(last_crew)
#
#     if len(last_crew) == m:
#         answer = last_crew[0] - 1
#     else:
#         answer = last
#
#     Hour = str(answer // 60)
#     Min = str(answer % 60)
#     if len(Hour) == 1:
#         Hour = '0' + Hour
#     if len(Min) == 1:
#         Min = '0' + Min
#     answer = Hour + ':' + Min
#     # print(answer)
#     return answer