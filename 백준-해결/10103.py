num = int(input())

p1 = 100
p2 = 100

for i in range(num):
    n1,n2 = map(int,input().split())
    if n1>n2:
        p2 = p2 - n1
    elif n1<n2:
        p1 = p1 - n2
    elif n1==n2:
        pass

print(p1)
print(p2)
