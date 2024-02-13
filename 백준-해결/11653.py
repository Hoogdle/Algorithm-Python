# 소인수 분해 
# 1보다 큰 자연수를 소인수들만의 곱으로 나타냄
# 소인수 == 소수 : 1 or 자기 자신으로 밖에 나누기 가능



num = int(input())

if num == 1:
    exit()

while True:
    i = 2
    while True:
        if num%i!=0:
            i = i+1
            continue
        elif num==i:
            print(i)
            exit()

        if num%i==0:
            num = num//i
            print(i)
            break





