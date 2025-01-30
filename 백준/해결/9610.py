num = int(input())
l = [0,0,0,0,0]
for i in range(num):
    n1,n2 = map(int,input().split())
    if n1==0 and n2==0:
        l[4] += 1
    elif n1==0 or n2==0:
        l[4] += 1
    elif n1>0 and n2>0:
        l[0]+=1
    elif n1<0 and n2>0:
        l[1]+=1
    elif n1<0 and n2<0:
        l[2]+=1
    elif n1>0 and n2<0:
        l[3]+=1
    
for index,item in enumerate(l):
    if index == 4:
        print(f'AXIS: {item}')
        break
    print(f'Q{index+1}: {item}')
    
    
        
