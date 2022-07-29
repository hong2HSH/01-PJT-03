import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input()) # 테스트 케이스의 수

for i in range(T):
    a = list(map(int,input().split())) # 카드번호 확인
    cnt = 1
    sum = 0
    for j in a: 
        if cnt % 2 == 0:
            sum += j
        else:
            sum += (j * 2)
        cnt += 1 # 카드번호가 홀수이면 *2를 해서 더하고 짝수이면 그냥 더해줌
    ans = str(10 - (sum % 10)) # N(ans)의 값을 확인
    ans = ans.replace('10','0') # 10은 0으로 대체
    print(f'#{i+1} {ans}')