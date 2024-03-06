# 1.자주 나오는 단어일수록 앞에 배치
# 2.길이가 길수록 앞에 배치
# 3.사전 순 앞이면 앞에 배치

######## 시간초과 ㅠㅠ

# M이상의 단어만 외운다.

# {배운점}
# set연산 : 문자열에도 적용가능

num_word,len_word = map(int,input().split())
### 첫 줄 완료
word_list = []
for i in range(num_word):
    s = input()
    if len(s)<len_word:
        continue
    word_list.append(s)


### 길이를 충족하지 않는 아이템 삭제 완료

# 우선순위 1번 
# : 단어 리스트를 돌며 maxcount을 찾는다.
# : maxcount에서 하나씩 빼며 같은 count 인 단어들을 '하나의 리스트' 로 저장한다
# 각각의 리스트를 하나의 리스트에 포함한다. ex[[],[],[]]

# 우선순위 2번
# : 리스트안의 각 리스트에서 max len 찾기 
# : max len에서 하나씩 빼며 같은 len을 갖는 단어들을 하나의 리스트로 저장
# : 각각의 리스트를 저장
# ex) [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]

# 우선순위 3번
# : 각 리스트에서 sort() 연산 (가나다 순으로 정렬)

# 우선순위 4번 
# 리스트 하나씩 출력

total = []

big = word_list.count(word_list[0])
for i in range(len(word_list)):
    if big < word_list.count(word_list[i]):
        big = word_list.count(word_list[i])



while big>0:
    sub_list = []
    for word in word_list:
        if big  == word_list.count(word):
            sub_list.append(word)
    sub_list = list(set(sub_list))
    if not sub_list:
        big-=1
        continue
    total.append(sub_list)
    big -= 1

### count 단위 리스트로 묶어 세팅완료
# [['banana', 'apple'], ['orange', 'kiwi']]
Final_total = []
for bag in total:
    big = len(bag[0])
    for item in bag:
        if len(item) > big:
            big = len(item)
    while big > 0:
        sub = []
        for item in bag:
            if big == len(item):
                sub.append(item)
        if not sub:
            big -= 1
            continue
        Final_total.append(sub)
        big -= 1

## count 및 길이 적용 완료
# [['seoul'], ['orange'], ['apple', 'ddaad']]
Real_Final = []
for bag in Final_total:
    bag.sort()
    Real_Final.extend(bag)

for value in Real_Final:
    print(value)
    




        


        
    


