import sys
sys.stdin = open('모음이 보이지 않는 사람.txt')

T = int(input())

for t in range(1, T+1):
    word = input()
    vowel = [97, 101, 105, 111, 117]
    result = ''
    for i in range(len(word)):
        if ord(word[i]) in vowel:
            continue
        result += word[i]
    print('#%d'%t, result)