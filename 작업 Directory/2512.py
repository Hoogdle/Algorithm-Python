# {배운점}
# :나누기 // 연산은 소수점 자리를 아예 버린다

num_city = int(input())
value = input()
value = list(map(int,value.split()))
sum_cost = 0
for i in value:
    sum_cost += i


available = int(input())

if sum_cost <= available:
    big = value[0]
    for i in value:
        if i>big:
            big = i
    print(big)
    exit()


value.sort()

small_list = []
alpha = -1
for item in value:
    if item == value[len(value)-1]:
        break
    small_list.append(item)
    small_sum = sum(small_list)
    key = (available-small_sum)//(len(value)-len(small_list))
    if alpha < key:
        alpha = key

### alpha가 최대가 될 때까지 하나씩 포인트업 
# 수정 필요함 조금씩 밀림
while True:
     if alpha * len(value) > available:
         alpha -= 1
         break
     elif alpha * len(value) > available:
         break
     
     else:
         alpha += 1

print(alpha)