# split() => return List
# int(), List형 변경불가
# map(int,input().split()), List data 각각을 int형으로


num = int(input())

for i in range(num):
    a,b = map(int,input().split()) #map 함수를 통해 리스트로 변환 된 값을 int로 각각 변환
    c = a+b
    print(f'Case #{i+1}: {a} + {b} = {c}')