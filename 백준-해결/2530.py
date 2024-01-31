# 합산을 '초'단위로 변환
# //, % 상위목록과 하위목록(use and remain)

h,m,s = map(int,input().split())
u = int(input())

c_s = h*60*60 + m*60 + s + u

c_h = c_s//3600
c_m = c_s%3600//60
c_s = c_s%3600%60

if c_h >= 24:
    c_h -= int(24*(c_h//24))

print(c_h,c_m, c_s)
