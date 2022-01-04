text=input()
i=0
'''
while text[i]!='r':
    print(text[i],end='')
    i=i+1
'''
for i in range(len(text)):
    if text[i] == 'r':
        break
    print(text[i],end='')
