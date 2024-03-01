# 팀의 점수 == 상위 4명
# 가장 낮은 점수를 얻는 팀 우승
# 만약 6명 참가 x 점수 계산 제외
# 동점인 경우 5 번째 주자가 가장 빨리 들어온 팀 우승
# 6명보다 많은 경우 없음 적어도 한 팀의 참가 인원은 6명이 이상 보장




# {배운점}
# 이중 반복문은 서로 다른 문자를 사용해야 한다.
# 반복문 안에서 정의된 데이터는 반복문 안에서만 사용가능하다.
# for 문에서 control 하는 리스트를 for문 안에서 삭제하는 경우 인덱스 에러 발생 가능
# [[1, 1], [2, 2], [4, 1]] 이런 꼴 또는
# [[1, 18, 9, 5], [2, -1, 0, 0], [3, 18, 10, 5], [4, -1, 0, 0]] 이런 꼴로
# 정리하면 생각보다 순서에 맞게 데이터를 정리하기 쉽다.

num_of_test = int(input())

for i in range(num_of_test):
    num_of_person = int(input())
    sequence =''
    sequence = input() # sequence는 등수 순서
    sequence = list(map(int,sequence.split()))
    team = list(set(sequence)) # team 은 팀의 목록
    team.sort()
    temp = [0]*len(team)
    team = list(zip(team,temp,temp,temp))
    team = list(map(list,team)) # [팀,count] 로 리스트화 #[[1, 0], [2, 0], [4, 0]]
    for j in range(num_of_person):
        for l in range(len(team)):
            if sequence[j] == team[l][0]:
                team[l][1] += 1
    # 팀 단위 count 완료 #[[1, 1], [2, 2], [4, 1]]
    team_of_less =[]
    for j in range(len(team)):
        if team[j][1]<6:
            team[j][1] = -1
            team_of_less.append(team[j][0])
        else:
            team[j][1] = 0
    # print(team_of_less)
    # 실격 팀의 count -1로 업데이트 #[[1, -1], [2, -1], [3, -1], [4, -1]]
    # 선택되는 팀은 count 0 으로 업데이트 #[[1, 0], [2, -1], [3, -1], [4, -1], [5, -1]]
    adder = 1
    for j in range(num_of_person):
        if sequence[j] in team_of_less:
            continue
        else:
            for l in range(len(team)):
                if sequence[j] == team[l][0] and team[l][1] >= 0:
                    team[l][1]+=adder
                    team[l][3]+=1
                    if team[l][3] == 5:
                        team[l][2] = adder
                        team[l][1] -= adder
                    elif team[l][3] > 5:
                        team[l][1] -= adder
                    adder+=1
    # print(team) #점수화(4번째 까지), 5번째 저장 완료 #[[1, 18, 9, 5], [2, -1, 0, 0], [3, 18, 10, 5], [4, -1, 0, 0]]
    team_of_result = []
    biggest_and_smallest = 0
    for j in range(len(team)):
        if team[j][1] > biggest_and_smallest:
            biggest_and_smallest = team[j][1]  
         
    for j in range(len(team)):
        if team[j][1] < biggest_and_smallest and team[j][1] != -1:
            biggest_and_smallest = team[j][1]
    # print(biggest_and_smallest)
    # 최소 점수 확보
    for j in range(len(team)):
        if biggest_and_smallest == team[j][1]:
            team_of_result.append(team[j])
    # 최소 점수를 갖는 팀 들만의 집합
    # print(team_of_result)


    # 결과물
    if len(team_of_result) == 1:
        print(team_of_result[0][0])
    elif len(team_of_result) > 1:
        smallest = team_of_result[0][2]
        index = 0
        for j in range(len(team_of_result)):
            if smallest>team_of_result[j][2]:
                index = j
                smallest = team_of_result[j][2]
        print(team_of_result[index][0])



    

        

  

    
                                

    

    

    
    

