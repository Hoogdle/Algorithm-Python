# 이중 for문 i와 j로 구별하기!


num = int(input())




for i in range(num):
    team = []
    n = int(input())
    s = list(map(int,input().split()))
    for i in range(n): # 팀 목록
        if s[i] not in team : team.append(s[i]) 
    team_count = [0]*len(team)
    team_result = [0]*len(team)
    team_5 =[0]*len(team)
    for i in range(n): # 각 팀의 완주 횟수
        team_count[team[i]-1]+=1
    for i in range(len(team_count)): # 6명 미만 팀 n/a로 변경
        if team_count[i]<6:
            index = i+1
            for i in range(n):
                if s[i]==index and isinstance(s[i],int):
                    s[i] = 'n/a'
    for i in range(n):
        count = 1
        if s[n] == 'n/a':
            pass
        else:
            team_5[s[n]-1] += 1
            team_result[s[n]-1] += count
            if team_5[s[n]-1] == 5:
                team_5[s[n]-1] = count
            count += 1
    
    for i in range(len(team_result)):
        value = []
        if team_result[i] == 0:
            pass
        else:
            value.append([i,team_result[i]])

    smallest = [value[0][0],value[0][1]]
    for i in range(len(value)):
        if value[i][1] < smallest:
            smallest = [value[i][0],value[i][1]]
    
    print(smallest)

    


    

        
        

            


        



