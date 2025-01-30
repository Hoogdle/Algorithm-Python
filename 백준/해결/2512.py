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

cal_list = [] # 기준(alpha)보다 작은 값들의 모임
for item in value:
    if item<alpha:
        cal_list.append(item)

smallsum = sum(cal_list)
biglen = num_city - len(cal_list)

while True:
    if alpha * biglen > available - smallsum:
        alpha -= 1
        break
    alpha += 1

print(alpha)