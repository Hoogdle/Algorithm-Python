s = input()
total_num = len(s)
num = len(s)-(len(s)//2)
#print(num)
result = 1

for i in range(num):
    if (s[i]!=s[total_num-(i+1)]):
        result = 0

print(result)