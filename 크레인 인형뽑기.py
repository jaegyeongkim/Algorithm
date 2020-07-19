def solution(board, moves):
    stack = list()

    cnt = 0
    for i in moves:
        i = i-1
        for j in range(len(board)):
            if board[j][i] > 0:
                stack.append(board[j][i])
                board[j][i] = 0
                break
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                cnt += 1
    answer = cnt*2
    return answer