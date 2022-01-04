# 특정 조건을 만족할 때와 만족하지 않은 때를 나누어 코드를 실행하는 조건문
# 조건이 참일 때= 실행, 조건이 거짓일 때= 실행하지 않음.
# if 조건:  -> 조건은 한 칸 띄어쓰기
#      실행코드 -> 한 블록 들여쓰기

# if
'''
num=int(input('숫자 하나 입력:'))

if num>0:
    print('{}은(는) 양수입니다.'.format(num))
'''

#if~else - else에는 조건을 적지 않는다. 
'''
num=int(input('숫자 하나 입력:'))

if num%2==0:
    print('{}은(는) 짝수입니다.'.format(num))
else :
    print('{}은(는) 홀수입니다.'.format(num))
'''

# if~elif => elif= else if 줄임. 추가적으로 범위를 나눌 것이 있으면 사용. 여러개 원하는 만큼 사용 가능.
# 윗부분에서 참이 되면 다음 조건 검사 하지 않음. 그대로 멈춤.
'''
age=int(input('나이 입력:'))

if age<=7:
    print('유아입니다.')
elif age<=19:
    print('청소년입니다.')
elif age>=20:
    print('성인입니다.')
'''

# if~elif~else => 위에 있는 조건들을 다 만족하지 않을 때 어떻게 하겠다. else에는 조건 적지 않음. 

text=input('알파벳 입력:')

if text.isupper():
    print('대문자')
elif text.islower():
    print('소문자')
else :
    print('대/소문자 구분 불가능')
    



















