import sys
sys.stdin = open('완주하지 못한 선수.txt')


def solution(participant, completion):
    participant.sort()
    completion.sort()
    is_last = True
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            is_last = False
            break

    if is_last:
        return participant[i + 1]
    return participant[i]


T = int(input())

for t in range(1, T+1):
    participant = list(map(str, input().split()))
    completion = list(map(str, input().split()))
    # print(participant, completion)
    print(solution(participant, completion))