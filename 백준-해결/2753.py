# 윤년 
# 4의 배수 and 100의 배수 아님 or 400의 배수

# ~윤년
# 위의 경우가 아닌 경우

num = int(input())

if num%4==0 and num%100!=0 or num%400==0:
    print(1)
else:
    print(0)   