# 한 줄에 하나씩 숫자 입력받기
'''
a=int(input('a 입력:'))
b=int(input('b 입력:'))
c=int(input('c 입려:'))

print(a,b,c,a+b+c)
'''

# 한 줄에 여러 개의 숫자 입력받기
'''
a,b,c=map(int,input('a b c 값 입력').split())

print(a,b,c,a+b+c)
'''

# 문자1.split(문자2) : 문자2를 기준으로 문자1을 자른다.
'''
text=input('날짜 입력 yyyy.mm.dd')
y,m,d=text.split('.')

print(text,y,m,d)
'''

# map(함수,집합 형태-iterable객체)-집합형태 안에 있는 것들을 앞의 함수로 다 적용시켜주는 함수.
'''
a,b,c=map(int,['1','2','3'])

print(a,b,c,a+b+c)
'''
# 하나씩 적용
'''
a,b,c=map(int,input('a b c값 입력').split()) #밑의 세줄을 한줄로 합쳐 놓은 형태

text=input('a b c값 입력') #제일 안쪽에서 시작
text=text.split()
a,b,c=map(int,text)

print(a,b,c,a+b+c)
'''

# 숫자 출력하기
'''
x=3
y=5

# print(x,y,x+y)
print('3과 5의 합은 8이다')
'''

# 숫자와 문자 함께 출력하기 (1) 콤마 & 형변환-콤마를 쓰면 자동으로 띄어쓰기가 됨. 추천하지 않음.
'''
print(x,'과',y,'의 합은',x+y,'이다.')

print(str(x)+'과 '+str(y)+'의 합은 '+str(x+y)+'이다.')

'''

# 숫자와 문자 함께 출력하기 (2) end='' - 줄바꿈을 없애는 것. 좋은 방법은 아님
'''
print(x,end='')
print('과 ',end='')
print(y,end='')
print('의 합은 ',end='')
print(x+y,end='')
print('이다.')
'''

# 숫자와 문자 함께 출력하기 (3) format() - 추천하는 방법임.
'''
print('{}과 {}의 합은 {}이다.'.format(x,y,x+y))
'''

# 연산자 우선 순위

'''
산술>관계>논리

지수,곱나눔,더하기빼기
not, and, or
'''

# 수학 관련 함수 - 7개

# 반올림 : round(a), round(a,b) - a: 반올림을 할 대상, b: 소수점 몇번째 자리까지. 
'''
print(round(3.33))
print(round(3.66))
print(round(3.66,1))
'''

# 절대값 : abs(a) - 양수로 나옴
'''
print(abs(3))
print(abs(-3))
'''
# 제곱 : pow(a,b) - a: 밑, b: 지수
'''
print(pow(3,2))
print(3**2)
'''
# 나눗3셈 : divmod(a,b) - 몫과 나머지를 모두 다 환함. 
'''
x,y=divmod(7,2)
print(x)
print(y)
'''
# 최대값 : max(a,b,c,d,...)
'''
print(max([7,5,1,3]))
'''
# 최소값 : min(a,b,c,d,...)
'''
print(min([7,5,1,3]))
'''
# 합 : sum(집합 형태:Iterable) - 값을 여러개 모아놓은 상태만 사용할 수 있음. list, tuple,...
print(sum([7,5,1,3]))













