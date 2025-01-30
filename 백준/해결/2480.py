n1,n2,n3 = map(int,input().split())

if n1==n2==n3:
    print(10000+n1*1000)
elif n1==n2:
    print(1000+n1*100)
elif n2==n3:
    print(1000+n2*100)
elif n1==n3:
    print(1000+n1*100)
else:
    if n1>n2:
        big = n1
    else:
        big = n2
    if big>n3:
        pass
    else:
        big = n3
    print(big*100)
