num1,num2,num3 = input().split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

print((num1+num2)%num3)
print(((num1%num3)+(num2%num3))%num3)
print((num1*num2)%num3)
print(((num1%num3)*(num2%num3))%num3)
