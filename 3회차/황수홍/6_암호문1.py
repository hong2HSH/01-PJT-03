import sys

sys.stdin = open("_암호문1.txt")

for i in range(10):
    a = int(input()) # 원본 암호문의 길이
    b = list(map(int,input().split())) # 원본 암호문
    c = int(input()) # 명령어의 개수
    d = list(input().split()) # 명령어

    for j in range(len(d)): # 쪼개진 d의 길이로 범위 설정
        if d[j] == 'I': # I가 키포인트 I로 암호변경 앞에서부터 차례대로 진행
            x = int(d[j+1]) # 문제에서 주어진 x, y 값을 받음
            y = int(d[j+2]) 
            for k in range(y): 
                b.insert(x+k,int(d[j+2+(k+1)])) # y개의 숫자를 b에 x의 위치 다음으로 삽입

    print(f'#{i+1} {" ".join(map(str,b[:10]))}') # 수정한 b값에서 10번째 자리까지만 출력
