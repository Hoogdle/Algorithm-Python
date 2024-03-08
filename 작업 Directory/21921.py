entire,during = map(int,input().split())


p_list = input()
p_list = list(map(int,p_list.split()))
### input data 세팅 완료

sum_list = []

big = 0
count = 0
### 최대 인덱싱 까지 세팅 완료
for i in range(len(p_list)-during+1):
    temp = sum(p_list[i:i+during])
    if temp>big:
        big = temp
        count = 1
        continue
    if temp == big:
        count +=1
    


if big == 0:
    print('SAD')
    exit()
print(big)
print(count)


