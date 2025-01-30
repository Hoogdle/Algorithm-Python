price,num,have = map(int,input().split())

value = have - price*num

if value>=0:
    print(0)
else:
    print(abs(value))