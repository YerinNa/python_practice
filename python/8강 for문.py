# 반복문 for문: 특정 범위만큼 코드를 반복 실행하는 조건문
# 열거형 데이터를 하나씩 변수 값에 대입하며 실행

# for 변수 in 열거형:
#     실행코드

# 열거형 자료란? 반복이 가능한 자료들, 값이 하나가 아니라 값이 여러개 모여 집합의 형태를 이루고 있는 데이터들. 

# range() 함수- for문에서 굉장히 많이 활용. 괄호 안의 수 모두 정수(int)만 가
# 숫자의 범위와 증감 값을 정하면 규칙적인 수들의 집합으로 만들어주는 함수.
# range(11) = 0~10까지 1씩 증가. 0,1,2,3,4,5,6,7,8,9,10
# range(1,11) = 1~10까지 1씩 증가
# range(1,11,2) = 1~11까지 2씩 증가. 1,3,5,7,9
# range()함수가 열거형 자리에 들어가게 되면 range()함수가 만들어낸 숫자를 하나씩 변수에 넣어서 for문이 실행시킴

# range() 연습

# 0,1,2,3,4
'''
range(5)

list(range(5))
'''
# 1,2,3,4,5,6,7,8,9,10
'''
list(range(1,11))
'''
# 3,6,9
'''
list(range(3,10,3))
list(range(3,11,3))
'''
# 5,4,3,2,1- 값이 올라갈때는 range 값 마지막에 +1, but 내려갈때는 -1을 해줌. 
'''
list(range(5,0,-1))
'''
# 10,5,0,-5,-10
'''
list(range(10,-11,-5))
'''

# for문- i,j,k 순으로 많이 사용.
'''
for i in range(10):
    print(i)
'''
# 1에서 n까지 출력
'''
n=int(input('n:'))

for i in range(1,n+1):
    print(i)
'''
# a에서 b까지 출력
'''
a,b=map(int,input('a b:').split())

for i in range(a,b+1):
    print(i)
'''
# n에서 0까지 출력

n=int(input('n:'))

for i in range(n,-1,-1):
    print(i)






















