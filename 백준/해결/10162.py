# 300 60 10

l=[0]*3 # a,b,c

time = int(input())

while True:
    if time == 0:
        r1,r2,r3=l
        print(r1,r2,r3)
        break

    if time-300>=0:
        time -= 300
        l[0] += 1
    elif time-60>=0:
        time -= 60
        l[1] += 1
    elif time-10>=0:
        time -= 10
        l[2] += 1
    else:
        print(-1)
        break

