'''
알파벳 소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하세요.
단, 파이썬의 내장 함수만 사용하여 구현하고 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

str = input()
d = {}

for i in str:
    d[i] = 0

for i in str:
    d[i] += 1

maxValue = max(d.values())
result = [x for x in d.keys() if d[x] == maxValue]

'''
# 리스트 내포 안쓰면
result = []
for x in d.keys():
    if d[x] == maxValue:
        result.append(x)
'''

if len(result) > 1:
    print('?')
else:
    print(result[0])