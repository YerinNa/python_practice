# 앞에서 배운 제어문과 함께 다양하게 활용되는 명령문
# continue, break, pass
# continue: 해당 단계만 건너뛰고 다음 단계로 간다.
# break: 제어문을 중단하고 빠져나간다
# pass: 아무 작업도 하지 않는다.

# continue
'''
for i in range(1,11):
    if i==5:
        continue
    print(i)
'''

# break
'''
for i in range(1,11):
    if i==5:
        break
    print(i)
'''

# pass-없는 거랑 결과가 똑같음. 코드를 큰틀만 잡아놓고 넘어가고 싶을 때 사용.
'''
for i in range(1,11):
    if i==5:
        pass
    print(i)
'''

# 비워두기
'''
n=int(input('n:'))

if n>0:
    #~~~~
else :
    #~~~~
'''
# 이렇게 하면 error 남

# 따라서 pass 넣음.

n=int(input('n:'))

if n>0:
    pass
else :
    pass













