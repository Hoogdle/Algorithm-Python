
# a 세자리, b 세자리
a = input()
b = input()
sum = 0

a = int(a)
b = int(b)

one = (b%100)%10
ten = (b%100)//10
hun = b//100

print(one*a)
sum += one*a

print(ten*a)
sum += ten*a*10

print(hun*a)
sum += hun*a*100

print(sum)