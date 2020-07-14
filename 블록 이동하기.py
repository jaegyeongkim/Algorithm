import sys
sys.stdin = open('블럭 이동하기.txt')

from collections import deque


def bfs(li, lj, ri, rj, board, N, visited):
    queue = deque()
    queue.append((li, lj, ri, rj, 0))
    visited[li][lj] = 1
    visited[ri][rj] = 1
    while queue:

        li, lj, ri, rj, cnt = queue.popleft()

        if lj > rj:
            lj, rj = rj, lj
        elif li > ri:
            li, ri = ri, li
        visited[li][lj] += 1
        visited[ri][rj] += 1
        if li == ri:    # 가로
            if li+1 < N:        # 아래
                if board[li+1][lj] == 0 and board[ri+1][rj] == 0:
                    if visited[li][lj] <= 2 or visited[ri+1][rj-1] <= 2:
                        queue.append((li, lj, ri+1, rj-1, cnt+1))
                        visited[li][lj] += 1
                        visited[ri+1][rj-1] += 1
                    if visited[li+1][lj+1] <= 2 or visited[ri][rj] <= 2:
                        queue.append((li+1, lj+1, ri, rj, cnt+1))
                        visited[li+1][lj+1] += 1
                        visited[ri][rj] += 1
                    if visited[li+1][lj] <= 2 or visited[ri+1][rj] <= 2:
                        queue.append((li+1, lj, ri+1, rj, cnt+1))
                        visited[li+1][lj] += 1
                        visited[ri+1][rj] += 1

            elif 0 <= li-1:     # 위
                if board[li-1][lj] == 0 and board[ri-1][rj] == 0:
                    if visited[li][lj] <= 2 or visited[ri-1][rj-1] <= 2:
                        queue.append((li, lj, ri-1, rj-1, cnt+1))
                        visited[li][lj] += 1
                        visited[ri-1][rj-1] += 1
                    if visited[li-1][lj+1] <= 2 or visited[ri][rj] <= 2:
                        queue.append((li-1, lj+1, ri, rj, cnt+1))
                        visited[li-1][lj+1] += 1
                        visited[ri][rj] += 1
                    if visited[li-1][lj] <= 2 or visited[ri-1][rj] <= 2:
                        queue.append((li-1, lj, ri-1, rj, cnt+1))
                        visited[li-1][lj] += 1
                        visited[ri-1][rj] += 1
        else:   # 세로
            if lj+1 < N:   # 오른쪽
                if board[li][lj+1] == 0 and board[ri][rj+1] == 0:
                    if visited[li][lj] <= 2 or visited[ri-1][rj+1] <= 2:
                        queue.append((li, lj, ri-1, rj+1, cnt+1))
                        visited[li][lj] += 1
                        visited[ri-1][rj+1] += 1
                    if visited[li+1][lj+1] <= 2 or visited[ri][rj] <= 2:
                        queue.append((li+1, lj+1, ri, rj, cnt+1))
                        visited[li+1][lj+1] += 1
                        visited[ri][rj] += 1
                    if visited[li][lj+1] <= 2 or visited[ri][rj+1] <= 2:
                        queue.append((li, lj+1, ri, rj+1, cnt+1))
                        visited[li][lj+1] += 1
                        visited[ri][rj+1] += 1

            elif 0 <= lj-1:
                if board[li][lj-1] == 0 and board[ri][rj-1] == 0:
                    if visited[li][lj] <= 2 or visited[ri-1][rj-1] <= 2:
                        queue.append((li, lj, ri-1, rj-1, cnt+1))
                        visited[li][lj] += 1
                        visited[ri-1][rj-1] += 1
                    if visited[li+1][lj-1] <= 2 or visited[ri][rj] <= 2:
                        queue.append((li+1, lj-1, ri, rj, cnt+1))
                        visited[li+1][lj-1] += 1
                        visited[ri][rj] += 1
                    if visited[li-1][lj] <= 2 or visited[ri-1][rj] <= 2:
                        queue.append((li-1, lj, ri-1, rj, cnt+1))
                        visited[li-1][lj] += 1
                        visited[ri-1][rj] += 1


        for d in range(4):          # 회전 X 이동
            nli = li + di[d]
            nlj = lj + dj[d]
            nri = ri + di[d]
            nrj = rj + dj[d]
            if 0 <= nli < N and 0 <= nlj < N and 0 <= nri < N and 0 <= nrj < N:
                if visited[nli][nlj] <= 2 or visited[nri][nrj] <= 2:
                    if board[nli][nlj] == 0 and board[nri][nrj] == 0:
                        if (nli == N-1 and nlj == N-1) or (nri == N-1 and nrj == N-1):
                            return cnt+1
                        queue.append((nli, nlj, nri, nrj, cnt+1))




def solution(board):
    N = len(board)
    visited = [[0] * N for _ in range(N)]

    answer = bfs(0, 0, 0, 1, board, N, visited)
    print(answer)
    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]  # 상 우 하 좌

solution(board)

# 목표 지검은 N-1, N-1
# 시작점은 (0,0), (0,1)
# 시작점을 0,1 로 하고
# bfs 로 하면 될듯한데