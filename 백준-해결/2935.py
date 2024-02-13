# 덧셈,곱셈만
# 제공되는 수 == 10의 제곱
# 제공되는 수의 길이 < 100

int1 = int(input())
op = input()
int2 = int(input())

if op == '+':
    print(int1+int2)
elif op =='*':
    print(int1*int2)