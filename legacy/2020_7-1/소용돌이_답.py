import sys
sys.stdin = open('소용돌이.txt')

r1, c1, r2, c2 = map(int, input().split())
cnt = (abs(r1-r2)+1)*(abs(c1-c2)+1)
position = {}
rl, ul, ll, dl = 1, -1, -1, 1
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0] # 우 상 좌 하

d = 0
i, j = (0, 0)
idx = 1
end = 0
while end != cnt:
    if r1 <= i <= r2 and c1 <= j <= c2:
        position[(i, j)] = idx
        end += 1
    idx += 1
    i += di[d]
    j += dj[d]

    if i == ul:
        d = 2
        ul -= 1
    elif i == dl:
        d = 0
        dl += 1
    elif j == rl:
        d = 1
        rl += 1
    elif j == ll:
        d = 3
        ll -= 1

max_length = len(str(max(position.values())))

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        string =' '*(max_length - len(str(position[i, j]))) + str(position[i, j])
        if j == c2:
            print(string)
        else:
            print(string, end=' ')

