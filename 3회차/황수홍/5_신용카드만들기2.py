import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input()) # 테스트 케이스의 수

list = ['3','4','5','6','9'] # 3,4,5,6,9를 리스트에 저장

for i in range(T):
    a = input() # 카드 번호 받음
    if a[0] not in list: # 첫번째 인덱스값이 리스트에 없을시 0출력
        print(f'#{i+1} 0')
    else:
        a = a.replace('-','') # "-"이 들어간 번호는 "-"를 제외
        if len(a) == 16: 
            print(f'#{i+1} 1')
        else:
            print(f'#{i+1} 0') # 16자리면 "1" 아니면 "0"