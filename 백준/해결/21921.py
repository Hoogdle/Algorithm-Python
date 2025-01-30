# 2024-06-24 월요일
# 덩어리 누적합으로 연산하여 해결

N,X = map(int,input().split())

l = list(map(int,input().split()))

start = 0

for i in range(X):
    start += l[i]

maximum = start
count = 1


for i in range(N-X):
    start = start - l[i] + l[i+X]
    if start > maximum:
        maximum = start
        count = 1
    elif start == maximum:
        count += 1

if(maximum==0):
    print('SAD')
else:
    print(maximum)
    print(count)
    