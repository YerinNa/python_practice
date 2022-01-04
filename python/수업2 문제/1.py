
a,b,c=map(int,input('a b c:').split())
if max(a,b,c)>100:
    print('{}은(는) 100보다 큽니다.'.format(max(a,b,c)))
elif max(a,b,c)<100:
    print('{}은(는) 100보다 작습니다.'.format(max(a,b,c)))
elif max(a,b,c)==100:
    print('{}은(는) 100과 같습니다.'.format(max(a,b,c)))
