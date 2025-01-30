# list 의 총합 함수
# sum(list)


num = int(input())

value = 0
for i in range(num):
    s = input()
    l = []
    for i in range(len(s)):
        if s[i] == 'O':
            if i==0:
                l.append(1)
            else:
                l.append(l[i-1]+1)
        else:
            l.append(0)
    value = sum(l)
    print(value)


        
