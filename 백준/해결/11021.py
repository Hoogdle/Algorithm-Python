# 파이썬은 문장 끝에 'end=/n' 이 생략됨. == 자동개행
# 자동 개행을 막으려면 문장 끝에 end='' 를 추가

num = input()
num = int(num)

for i in range(0,num):
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(f'Case #{i+1}: ',end='')
    print(a+b)