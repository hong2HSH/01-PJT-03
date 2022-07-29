import sys

sys.stdin = open("_소득불균형.txt")

T = int(input()) # 테스트 케이스의 수

for i in range(T):
    sum = 0
    cnt = 0
    N = int(input()) # 각 테스트별 사람 수
    M = input().split() # 사람들의 소득
    for j in M:
        sum += int(j) # 사람들의 소득을 모두 더함
    average = sum / N # 소득의 평균 확인
    for k in M: 
        if int(k) <= average:
            cnt += 1 # 소득이 평균이하인 사람들을 카운트
    print(f'#{i+1} {cnt}')