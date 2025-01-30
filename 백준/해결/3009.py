# count 함수 
# 반복 가능한 객체에서 사용 가능
# name.count(contents)


x = []
y = []

for i in range(3):
    n1,n2 = map(int,input().split())
    x.append(n1)
    y.append(n2)

v1,v2 = [0,0]

for i in range(3):
    if x.count(x[i]) == 1:
        v1 = x[i]
    if y.count(y[i]) == 1:
        v2 = y[i]

print(v1,v2)



