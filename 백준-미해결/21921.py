# entire,during = map(int,input().split())


# p_list = input()
# p_list = list(map(int,p_list.split()))
# ### input data 세팅 완료

# sum_list = []

# ### 최대 인덱싱 까지 세팅 완료
# for i in range(len(p_list)-during+1):
#     temp = sum(p_list[i:i+during])
#     sum_list.append(temp)

# ### sort함수가 시간을 많이 잡아 먹음
# sum_list.sort()
# biggest = sum_list[len(sum_list)-1]
# if biggest == 0:
#     print('SAD')
#     exit()

# ### count 함수를 대신해 마지막 인덱스 부터 시작, 시간절약
# count = 0
# end = len(sum_list)-1
# while True:
#     if sum_list[end] != sum_list[end-1]:
#         count += 1
#         break
#     count += 1 
#     end -= 1

# print(biggest)
# print(count)


### 최적의 코드 하지만 시간초과 ㅠㅠ

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







