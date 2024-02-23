while True:
    n = int(input())
    if n==-1:
        break
    value = 0
    l = []
    for i in range(1,n):
        if n%i==0:
            l.extend([i,n//i])
    l = set(l)
    l = list(l)
    l.sort()
    l.remove(n)
    value = sum(l)
    l = map(str,l)
    if value == n:
        s = " + ".join(l)
        print(f'{n} = {s}')
    else:
        print(f'{n} is NOT perfect.')

