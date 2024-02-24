num = int(input())


for i in range(num):
    d = {}
    n = int(input())
    for j in range(n):
        s,q = input().split()
        q = int(q)
        d[s] = q
    big = 0
    s = ''
    for item,value in d.items():
        if value>big:
            s = item
            big = value
        
    print(s)

    
        