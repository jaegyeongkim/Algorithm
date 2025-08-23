def solution(record):
    arr = []
    for i in range(len(record)):
        arr.append(list(map(str, record[i].split())))

    display = []
    nickname = {}
    for i in range(len(arr)):
        if arr[i][0] == 'Enter':
            display.append([arr[i][1], '님이 들어왔습니다.'])
            nickname[arr[i][1]] = arr[i][2]
        elif arr[i][0] == 'Leave':
            display.append([arr[i][1], '님이 나갔습니다.'])
        elif arr[i][0] == 'Change':
            nickname[arr[i][1]] = arr[i][2]

    answer = []
    for i in range(len(display)):
        answer.append(str(nickname[display[i][0]]) + str(display[i][1]))

    return answer