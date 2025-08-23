import sys
sys.stdin = open('모의고사.txt')


def solution(answers):
    student = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    correct = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == student[0][i%len(student[0])]:
            correct[0] += 1
        if answers[i] == student[1][i % len(student[1])]:
            correct[1] += 1
        if answers[i] == student[2][i % len(student[2])]:
            correct[2] += 1
    max_num = max(correct)
    answer = []
    for i in range(len(correct)):
        if correct[i] == max_num:
            answer.append(i+1)

    return answer

T = int(input())

for t in range(1, T+1):
    answers = list(map(int, input().split()))
    print(solution(answers))
