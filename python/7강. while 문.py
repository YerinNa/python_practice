# while 문
# 무한루프, n번 반복하기, ~까지 반복하기
# 특정 조건을 만족할 때 코드를 반복 실행하는 조건문
# 조건이 참일 때= 반복 실행, 조건이 거짓일 때= 반복 종료

# while문
'''
print('a가 0보다 같거나 크면 실행, 작으면 정지')
a=int(input('a:'))

while a>=0:
    print('실행')
    a=int(input('a:'))
'''

# 무한루프 - 종종 발생하는 실수, 발생시키지 않으려면 조건에 들어가는 값이 처음엔 참이었을지라도
# 안쪽에서 변경이 될 가능성이 있어야함.
# 즉, 거짓으로 바뀌어서 while 문을 끝낼 수 있는 장치가 필요함. 위의 식에서는 사용자가 값을 직접 입력하게 하는 것이 장치임.
'''
a=10

while a>0:
    print('실행')
'''

# n번 반복하기 - n에 숫자가 들어갈 경우 양수이면 true, 0 포함 음수이면 false 역할을 함.
'''
n= int(input('n:'))

while n:
    print(n)
    n=n-1
'''

# ~까지 반복하기
# (1) 1~10까지 숫자 반복하기
'''
n=1

while n<=10:
    print(n)
    n=n+1
'''

# (2) yes를 입력하면 반복하기
'''
text='yes'

while text=='yes':
    text=input('yes 입력 시 반복')

print('종료')
'''

# (3) e 또는 E가 입력될 때까지 반복하기
text= input('e 또는 E 입력 시 종료')

while text!='e' and text!='E':
    text=input('e 또는 E 입력 시 종료')

print('종료')


# while 문을 제일 어려워 함. 
















