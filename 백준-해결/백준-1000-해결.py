# 값을 입력 : input() 사용
# input()의 데이터는 str로 저장됨.
# int 값을 다루려면 int() 형변환 사용
# input().split() 으로 두 변수에 값을 한 번에 넣기 가능!

num1,num2 = input().split()

print(int(num1)+int(num2))