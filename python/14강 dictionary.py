#dictionary(사전형)
#dic={키:값, 키:값, 키:값}, 딕셔너리의 기본 형태. 리스트, 튜플, 세트와 달리 키(key)와 값으로 이루어짐.

#딕셔너리 만들기

dic={}
dic=dict()

#딕셔너리 특징

dic={'kor':80,'eng':90,'mat':77} #키와 값이 쌍으로 이루어져 있지 않으면 set가 됨.
dic['kor']
dic['kor']=85    #값 변경
dic['sci']=92    #값 추가

dic[0]  #인덱스로 값을 못 꺼냄. 키 값으로 넣어야 꺼낼 수 있음. 


#딕셔너리 활용

del dic['mat']          #삭제하기
dic.clear()             #전체 삭제
'eng' in dic            #확인하기 (키 기준)
len(dic)                #전체 개수

dic.keys()              #모든 키 얻기
dic.values()            #모든 값 얻기
dic.items()             #모든 순서쌍 얻기, 맨 바깥은 list나 tuple 형태로 감싸지는데 키와 값은 튜플 형태로 묶임. 



# 세가지 모두 키 값만 나옴. 값들을 가지고 오고 싶으면 list(dic.values()), tuples(dic.values()), set(dic.values()) 사용.
tuple(dic)           
list(dic)
set(dic)

li=['ab','cd','ef']        #짝이 맞아야 dictionary 형태로 바꿀 수 있음. 2쌍으로 맞춰야함.
dict(li)

# 안되는 예임.
li=['ab','cd','eff']
li=['abc','cde','eff']


li=[['a',1],['b',2],['c',3]]
dict(li)






