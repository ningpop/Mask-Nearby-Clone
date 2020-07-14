'''
정수 N이 입력 값으로 주어지면 (0<N<10) 그 다음 N번째 줄에
다음과 같이 출력되게 프로그램을 작성하세요.

입력: 9

1 3 5 7 9
 2 4 6 8
1 3 5 7 9
 2 4 6 8
1 3 5 7 9
 2 4 6 8
1 3 5 7 9
 2 4 6 8
1 3 5 7 9
'''

N = int(input())

for i in range(1, N+1):
    for j in range(1, N+1):
        if i%2 != 0:
            if j%2 != 0:
                print(j, end='')
            else:
                print('  ', end='')
        else:
            if j%2 != 0:
                print('  ', end='')
            else:
                print(j, end='')
    print()