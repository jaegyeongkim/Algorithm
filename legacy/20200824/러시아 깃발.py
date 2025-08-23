import sys
sys.stdin = open('러시아 깃발.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    flag = list(input() for _ in range(N))
    max_cnt = 2500
    # 흰 영역
    for i in range(N-2):
        # 파랑 영역
        for j in range(i+1, N-1):
            cnt = 0
            # 빨강 영역
            for w in range(i+1):
                for m in range(M):
                    if flag[w][m] != 'W':
                        cnt += 1
            for b in range(i+1, j+1):
                for m in range(M):
                    if flag[b][m] != 'B':
                        cnt += 1
            for r in range(j+1, N):
                for m in range(M):
                    if flag[r][m] != 'R':
                        cnt += 1
            if max_cnt > cnt:
                max_cnt = cnt
    print('#%d'%t, max_cnt)

