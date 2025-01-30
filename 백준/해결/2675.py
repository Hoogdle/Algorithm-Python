# 서로다른 데이터를 '공백'으로 나누어 입력 받는 경우
# split 함수를 쓰고 추후에 형변환
# count,s = input().split()
# count = int(count)

num = int(input())

for i in range(num):
    count,s = input().split()
    count = int(count)
    n_s = ''
    for j in range(len(s)):
        n_s += s[j]*count
    print(n_s)

        
        
