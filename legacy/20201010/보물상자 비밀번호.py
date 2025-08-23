import sys
sys.stdin = open('보물상자 비밀번호.txt')

def rotate():
    new_arr = [0] * N
    for n in range(N):
        new_arr[n] = arr[n]
    for n in range(N):
        arr[n] = new_arr[n-1]
    hextodec()

def hextodec():
    for i in range(0, len(arr), N//4):
        hex = ''
        for k in range(N//4):
            hex += arr[i+k]
        dec = 0
        for j in range(len(hex)):

            dec += hex_dic[hex[j]]*(16**(N//4-j-1))

        if dec not in dec_list:
            dec_list.append(dec)

hex_dic = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input())
    dec_list = []
    hextodec()

    for i in range(N-1):
        rotate()
    dec_list.sort(reverse=True)
    print('#%d'%t, dec_list[K-1])
