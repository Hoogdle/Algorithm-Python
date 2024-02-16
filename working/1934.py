# input() => 문자열로 저장
# split() => 동시에 입력, 기본적으로 '공백' 기준
# map(int,) => 각각의 문자열을 정수로
# n1,n2 = map(int,input().split())

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

    if small == 1:
        print(small*big)
        continue

    l = []


    