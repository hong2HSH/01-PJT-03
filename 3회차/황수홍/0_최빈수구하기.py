import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input()) # 테스트 케이스의 수

for i in range(T):
    Tc = int(input()) # 각 테스트 케이스
    list = input().split() # 테스트 케이스의 점수
    count = dict() # 같은 점수 세기위한 딕셔너리
    for i in list:
        if i not in count:
            count[i] = 0
        count[i] += 1
    M = max(count, key=count.get)
    print(f'#{Tc} {M}') # 출력