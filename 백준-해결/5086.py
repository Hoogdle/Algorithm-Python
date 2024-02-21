while True:
    n1,n2 = map(int,input().split())
    if n1==0 and n2==0:
        break
    if n2%n1==0:
        print('factor')
        continue
    elif n1%n2==0:
        print('multiple')
        continue
    else:
        print('neither')