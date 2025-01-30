# input은 문자열을 반환
# split은 조건 기준 나눠서 리스트로 반환
# map int로 각각의 리스트의 컨텐츠를 int로 변환
# 리스트의 값은 다변수에 자동 할당 됨

num = int(input())

for i in range(num):
    r,e,c = map(int,input().split())
    if r>e-c:
        print('do not advertise')
    elif r==e-c:
        print('does not matter')
    else:
        print('advertise')
    
