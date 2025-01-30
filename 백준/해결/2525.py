h,m = map(int,input().split())
u = int(input())

c_m = h*60+m+u

c_h = c_m//60
c_m = c_m%60

if c_h >= 24:
    c_h -=24

print(c_h,c_m)

