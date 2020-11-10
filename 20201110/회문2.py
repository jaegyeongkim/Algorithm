import sys
sys.stdin = open('회문2.txt')
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    arr1 = list(zip(*arr))
    res = 0
    c_tmp = 0
    r_tmp = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if arr[i][j] == arr[i][99-k]:
                    cnt = 0
                    while 1:
                        if arr[i][j+cnt] != arr[i][99-k-cnt]:
                            break
                        cnt += 1
                        if j+cnt == 100:
                            break
                        elif 99-k-cnt < 0:
                            break
                    if res < cnt:
                        res = cnt

                if arr1[i][j] == arr1[i][99-k]:
                    cnt = 0
                    while 1:
                        if arr1[i][j+cnt] != arr1[i][99-k-cnt]:
                            break
                        cnt += 1
                        if j+cnt == 100:
                            break
                        elif 99-k-cnt < 0:
                            break
                    if res < cnt:
                        res = cnt


    print('#%d'%tc, res)