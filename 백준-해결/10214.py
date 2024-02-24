num = int(input())

for i in range(num):
    y = 0
    k = 0
    for i in range(9):
        ny,nk = map(int,input().split())
        y = y + ny
        k = k + nk
    if(y>k):
        print('Yonsei')
    elif(y<k):
        print('Korea')
    elif(y==k):
        print('Draw')
