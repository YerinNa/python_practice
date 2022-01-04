text=input()

if len(text)>10:
    print('입력된 문자의 길이는 10보다 큽니다.')
elif len(text)<10:
    print('입력된 문자의 길이는 10보다 작습니다.')
elif len(text)==10:
    print('입력된 문자의 길이는 10과 같습니다.')
