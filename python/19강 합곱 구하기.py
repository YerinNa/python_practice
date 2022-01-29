# 합 구하기
# 숫자 n을 입력받아 1~n까지 합 구하기
'''
n=int(input('n:'))
s=0

for i in range(1,n+1):
    s=s+i

print(s)
'''

# 곱 구하기
# 숫자 n을 입력받아 1~n까지 곱 구하기
'''
n=int(input('n:'))
s=1

for i in range(1,n+1):
    s=s*i

print(s)
'''

# 값 누적하기
# 0을 입력할때까지 반복해서 숫자를 입력받아 합 구하기


n=int(input('n:'))
s=0

#NYR
while True:
    s=s+n
    n=int(input('n:'))
    if n==0:
        break
print(s)

# 실제 답
while n!=0:
    s=s+n
    n=int(input('n:'))
print(s)

# 문제 이해 잘못함
while True:
    s=s+n
    if n==0:
        break
    print(s)
    n=int(input('n:'))

    




















