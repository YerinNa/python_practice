# 리스트 만들기
'''
li=[]
li=list()
'''
# 리스트 인덱스
'''
li=['a','b','c']

li[0]
li[1]
li[2]
li[2]='d'
'''

#리스트 활용
li=['a','b','c','d','e']

li.index('c')  # 위치 찾기

li.append('f')  # 추가하기1, 몇번째에 넣을 것인지에 대한 값은 없음. 항상 맨끝에 추가됨. 
li.insert(0,'aa')  # 추가하기2, 원하는 곳에 넣고 싶을 때 사용

li.remove('aa')  # 삭제하기1, 값을 기준으로
del li[2]  # 삭제하기2, 번호를 기준으로 

'b' in li  # 확인하기, true/false 값으로 나옴. 

len(li)  # list가 갖고 있는 전체 개수, list가 반복문에 들어갔을 때, 특히 for문에 들어갔을 때 같이 많이 사용. 

li.count('a')  # 개수 세기



num=[1,2,3,4,5,9,7,6,8,10]

sum(num)  # 합구하기
min(num)  # 최소값
max(num)  # 최대값

num.reverse()  # 역순 만들기, 그대로 뒤집는 것.

num.sort()  # 오름차순 정렬, 작은것부터 크게. 괄호 안에 reverse=False 들어가도 됨(생략 가능)
num.sort(reverse=True)  # 내림차순 정렬, 큰것부터 작게 


















