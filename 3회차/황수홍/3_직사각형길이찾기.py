import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input()) # 테스트 케이스의 수

for i in range(T):
    a, b, c = input().split() # 세변의 길이를 받음
    a = int(a)
    b = int(b)
    c = int(c) # 세변의 길이를 정수형으로 변환
    if a == b :
        print(f'#{i+1} {c}')
    elif a == c :
        print(f'#{i+1} {b}')
    elif b == c :
        print(f'#{i+1} {a}') 

# 직사각형의 특성상3변의 길이에서 한번나온 길이가 나머지 한변의 길이