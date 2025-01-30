num = int(input())

for i in range(num):
    n1,n2 = map(int,input().split())
    if n1>n2:
        big = n1
        small = n2
    elif n1<n2:
        big = n2
        small = n1
    else:
        print(n1)
        continue
    if small==1:
        print(small*big)
        continue
    l=[]
    while True:
        i=2
        count = 0
        while not(small%i==0 and big%i==0):
            if i==small:
                l.extend([big,small])
                count = 1
                break
            i = i+1
        if count == 1:
            break
        if(small%i==0 and big%i==0):
            big = big//i
            small = small//i
            l.extend([i])
            if small==1:
                l.extend([small,big])
                break
            continue

    result = 1
    for k in l:
        result = result*k
    print(result)
