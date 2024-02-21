num = int(input())

win = 0
lose = 0

for i in range(num):
    k = int(input())
    if(k==1):
        win += 1
    else:
        lose += 1

if(win>lose):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')