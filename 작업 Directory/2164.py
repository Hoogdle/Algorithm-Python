# {배운점}
# - 시간측정
#: time.time()을 사용, start 와 end를 time()으로 측정후 end-start로 측정
#: 시간은 사용자의 입력을 기다리는 시간도 포함이 된다.   

# - del
# : 첫 번째 인덱스만 삭제한다 하더라도 다른 인덱스들이 한 칸씩 앞으로 움직여양 하기에 O(n) 소요
        
# de-queue??

from time import time

num_of_card = int(input())
card_list = []
for i in range(num_of_card):
    card_list.append(i+1)

# max 숫자를 받고 추가할 때 : 0.03초
start = time()



end = time()
print(end-start)
