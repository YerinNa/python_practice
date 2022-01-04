# if if/ for if/ while if/ for for

# if if
'''
age=int(input('나이입력:'))

if age<=7:
    print('유아입니다.')
elif age<=19:
    print('청소년입니다.')
    if age<=13:
        print('초등학생')
    elif age<=16:
        print('중학생')
    else:
        print('고등학생')
else:
    print('성인입니다.')
'''

# for if- 반복을 하는 도중에 체크를 해야할 때, 굉장히 많이 사용. 
'''
n=int(input('n:'))
for i in range(1,n+1):
    if i%3==0:
        print('X')
    else:
        print(i)
'''

# while if
'''
num1=0
num2=int(input('n:'))

while True:
    num1=num1+1
    print(num1)
    if num1==num2:
        break
'''
# 위의 제어문 무한 루프임.= while True

# for for- 주사위 2개를 던져서 나올 수 있는 눈의 경우의 수를 모두 구하는 프로그램.  

for i in range(1,7):
    for j in range(1,7):
        print(i,j)

# 총 36개의 경우의 수가 나옴. 
# i 값이 1인 상태에서 안쪽에 있는 코드를 실행하려고 보니 또 for문이 있음. 그래서 i가 1인 상태에서 j는 1~6 한번 반복.



# 위의 4가지 많이 씀. 














        
