# 여러 데이터를 입력 => input().split()
# List.sort() 함수 => list 값들을 오름차순으로 정렬

int1, int2, int3 = map(int,input().split())

l = [int1,int2,int3]

l.sort()
print(l[1])