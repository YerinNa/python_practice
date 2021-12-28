# 문자열 인덱스 - 양수는 0번부터 시작, 음수로 시작할 시 맨 뒤가 -1, 실수가 오면 안됨. 
'''
text='abc'

print(text[-3]) == text[0]
print(text[-2]) == text[1]
print(text[-1]) == text[2]
print(text[3])
print(text[2.0])
'''
# 문자열 슬라이스 - 문자를 잘라서 가져옴, 문자열 개수 셀 시 공백도 1개로 포함함. 

text='abcde fgh ijk'
# 인덱스 2개를 가지고 하는 과정 
# text[시작:끝+1]-> 시작~끝
'''
print(text[2:5])
print(text[1:8])
print(text[-5:-1]
print(text[5:]) # 5번째부터 끝까지
print(text[:5]) # 첫번째(즉 0번)부터 5번째 앞까지
print(text[:]) # 처음부터 끝까지
'''
# 인덱스 3개가 들어가는 경우
# print(text[2:5:?]) 앞의 2개는 위와 같음. 마지막은 문자를 가지고 올 문자들의 간격을 뜻함.
# 1의 간격일 경우 1개씩, 2의 간격일 경우 2개 중 1개씩, 3은 3개 중에 1개씩
# 음수일 경우 뒤에서부터, 범위 잘 보기 
'''
print(text[0:8:2]) -> acef
print(text[1:8:2]) -> bd g
print(text[8:0:-1])
print(text[::-1]) # 문자 순서가 뒷부분부터 뒤집혀서 나옴
'''

# 문자열 method - 10가지

# 1. 출력 지정 : format(a,b,c,...)
'''
text='abcde {} {}'
print(text.format('ABC',123))
'''
# 2. 대체하기 : replace(a,b) - a: 바꾸고 싶은 대상, b: 바꾸고 싶은 값, 한 자리 뿐만 아니라 여러자리도 됨. 
'''
text='abcde ABC ABC'
print(text.replace('ABC','KKK'))
'''
# 3. 자르기 : split(a)
'''
text='abcde A/B/C A.B.C'
a,b,c=text.split('/')
print(a)
print(b)
print(c)
'''
# 4. 합치기 : a.join() - list에 있는 것들을 합쳐서 문자열로 만들 때 많이 사용.
'''
text='abcde'
print('/'.join(text))
'''
# 5. 개수 확인하기 : count(a)
'''
text= 'abcde ABC ABC'
print(text.count('a'))
print(text.count('A'))
print(text.count('1'))
'''
# 6. 제거하기 : strip(a)/lstrip(a)/rstrip(a) - 문자의 맨 앞쪽이나 맨 뒷부분에 거슬리는 부분이 있으면 제거해줌.
# 양쪽 제거/왼쪽부터 제거/오른쪽부터 제거/괄호가 비어있으면 공백 제거, 중간에 있는 것들은 제거하지 못함. 
'''
text='***ab**cde*****'
print(text.strip('*'))
print(text.lstrip('*'))
print(text.rstrip('*'))
'''
# 7. 인덱스 찾기 : find(a)/rfind(a)/index(a)/rindex(a)
# 둘다 내가 찾는 값을 찾아줌. r이 붙으면 오른쪽, 없으면 왼쪽부터
# 둘의 차이점은 find는 없는 것을 찾으라고 할 때 -1을 리턴하고 index는 error를 냄. 
'''
text='ABC ABC'
print(text.find('d'))
print(text.rfind('d'))
print(text.index('d'))
print(text.rindex('d'))
'''
# 8. 확인하기 : isalpha()/isdigit()/isalnum()/isupper()/islower()
# 반환을 모두 true or false로 함.
# 알파벳으로만/숫자로만/숫자 또는 알파벳의 조합으로/대문자로/소문자로 이루어졌는지 확인할 수 있다.
'''
text1='ABCabc123'
text2='123'
text3='ABC'
text4='abc'

print(text4.isalpha())
print(text4.isdigit())
print(text4.isalnum())
print(text4.isupper())
print(text4.islower())
'''
# 9. 대/소문자 만들기 : upper()/lower()
'''
text='ABCabc'
print(text.upper())
print(text.lower())
'''
# 10. 0 채우기 : zfill() - 자릿수가 정해져있는 경우에 사용. 필요한 자릿수 만큼 숫자를 넣어줌

y='2020'
m='3'
d='1'

print(y.zfill(4))
print(m.zfill(2))
print(d.zfill(2))

# 억지로 외울 필요 없음. 












