import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input()) # 테스트 케이스의 수

for i in range(T):
    a = input() # 각 테스트 케이스
    a = a[::-1] # a를 뒤집어줌
    list = [] # .append로 값을 받아주기위한 리스트
    for j in a:
        if j == 'b':
            list.append('d')
        elif j == 'd':
            list.append('b')
        elif j == 'p':
            list.append('q')
        elif j == 'q':
            list.append('p') # 각각의 문자들을 대체
    print(f"#{i+1} {''.join(list)}")