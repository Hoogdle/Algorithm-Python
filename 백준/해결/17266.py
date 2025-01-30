# 인식이 0~N 가로등 설치 요구
# M : 가로등 설치 갯수
# x : 가로등의 위치
# 가로등의 높이만큼 주변을 비출 수 있다.
# 가로등의 높이 가격 비례 => 최소한의 노핑로 굴다리 길 0~N 밝히기
# 최소한의 높이?

# 모든 가로등의 높이가 같고 정수이다.

# if 높이 a 왼쪽 오른쪽을 각각 a만큼 비춤


## {배운점}
# 소수점 첫째자리'로' 반올림 => round(number,1)
# 소수점을 .5를 기준점으로 하여 정수부로 반올림 => round(number)
# 이 때 값이 (정수부).5 인 경우에는 짝수가 되는 방향으로 반올림 됨
# ex) round(2.5) => 2 // round(3.5) => 4


length = int(input()) # 굴다리의 길이
num_of_light = int(input()) # 가로등의 갯수
place_of_light = input() # 가로등의 위치
place_of_light = list(map(int,place_of_light.split()))
for_comparison = []

for_comparison.extend([place_of_light[0],length-place_of_light[len(place_of_light)-1]])
# print(for_comparison)
# 점 0과 첫번째 가로등 반영
# 마지막 점과 마지막 가로등 거리 반영
for i in range(num_of_light):
    if i == num_of_light-1:
        break
    if (place_of_light[i+1]-place_of_light[i])/2 == (place_of_light[i+1]-place_of_light[i])//2 + 0.5:
        for_comparison.append((place_of_light[i+1]-place_of_light[i])//2+1)
    for_comparison.append(round((place_of_light[i+1]-place_of_light[i])/2))
    # print(for_comparison)
# (각 가로등의 길이)/2 또한 추가 (모두 추가 됌)

for_comparison = list(set(for_comparison))

biggest = for_comparison[0]
for i in range(len(for_comparison)):
    if for_comparison[i]>biggest:
        biggest = for_comparison[i]

print(biggest)
