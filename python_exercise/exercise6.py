'''
while문과 for문 중첩을 사용해서 구구단 프로그램을 만들어 봅시다.
전체를 출력하는 구구단이 아니라 1을 입력하면 홀수 단(3, 5, 7, 9),
2번을 입력하면 짝수 단(2, 4, 6, 8), 3번을 입력하면 종료, 그 외의
숫자를 입력하면 처음부터 다시 입력되게 하는 프로그램을 만들어 보세요.
(단, 1번과 2번은 gugudan1(), gugudan2()라는 함수로 만들어 봅시다.)
'''

title = '''
구구단 프로그램을 실행합니다.
1. 홀수 구구단
2. 짝수 구구단
3. 종료
'''

def gugudan1():
    for i in range(2, 10):
        if i%2 != 0:
            print(f'\n{i}단')
            for j in range(1, 10):
                print(f'{i} * {j} = {i*j}')

def gugudan2():
    for i in range(2, 10):
        if i%2 == 0:
            print(f'\n{i}단')
            for j in range(1, 10):
                print(f'{i} * {j} = {i*j}')

while True:
    print(title)
    num = int(input("숫자를 입력하세요: "))

    if num == 1:
        gugudan1()
    elif num == 2:
        gugudan2()
    elif num == 3:
        print("프로그램을 종료 합니다.")
        break
    else:
        print("잘못 입력하셨습니다. 1 ~ 3번 숫자를 입력하세요.")
        continue