# 여러 데이터를 한번에 -> input().split()
# input 값을 공백으로 구분 해야.. -> input().split()
# 반환 값은 list형
# 데이터는 str 형
# str이 list안에 넣어진채로 반환

# map 반환값 == map 객체
# list로 활용하려면 list()로 변환

# 소수점 출력
# 문자열 안에 넣어야 함.
# f-string, f'{변수명:.2f}'
# .format, '{:.2f}'.format(변수)



num = int(input())

for i in range(num):
    l = input().split()
    n = float(l[0])
    for j in range(len(l)):
        if l[j] == '@':
            n *= 3
        elif l[j] == '%':
            n += 5
        elif l[j] == '#':
            n -= 7
    print(f'{n:.2f}')

