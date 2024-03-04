# 알고리즘
# 1. 첫번째 인덱스가 두번째 인덱스 보다 크다면 l1 만큼만 채우면 된다.
# 2. i,j,k가 순서대로 있을 때 j>i>k (ex, 3,4,2) 라면 j는 l(i~j)와 l(j~k)만큼만 가면된다.
# 즉 해당 리스트 원소에서 next 원소들을 탐색해 자신보다 작은 원소가 나올만큼만 기름을 충전하면 된다.
# 첫 번째 경우는 특별 케이스로 2가지로 나뉜다.

num_city = int(input())
len_list = []
cost_per_city = []

str_len = input()
len_list = list(map(int,str_len.split())) #거리 저장완료
str_cost = input()
cost_per_city = list(map(int,str_cost.split())) #거리 저장완료
print(len_list)
print(cost_per_city)
