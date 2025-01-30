# '적어도' m의 최솟값
#  i = m / a
#  m = i*a 

# i 반올림 O => i-1
# m = (i-1)*a
# real i > i - 1 (case in 반올림O)
# real m = real i * a
# m < real m
# so that m+1

# 수학적 수식, 논리로 풀어나가기




A,I = map(int,input().split())

if I == 0:
    print(0)
    exit()

M = (I-1)*A

print(M+1)