# 숫자가 섞이는 경우 ex) 컴퓨터는 0부터 실제 리스트는 1부터
# : 임의의 값을 0번째 인덱스에 추가하여 리스트와의 대칭을 맞춘 후 
# : 해결하는 것이 복잡하지 않고 좋음


def change(l,n):
    if l[n]==0:
        l[n]=1
    else:
        l[n]=0

def result(s,n_s):
    pn = 0
    nn = 20
    if n_s>80:
        while nn<=100:
            s[pn:nn] = list(map(str,s[pn:nn]))
            nt = ' '.join(s[pn:nn])
            print(nt)
            pn += 20
            nn += 20
    elif n_s>60:
        pn = 0
        nn = 20
        while nn<=80:
            s[pn:nn] = list(map(str,s[pn:nn]))
            nt = ' '.join(s[pn:nn])
            print(nt)
            pn += 20
            nn += 20
    elif n_s>40:
        pn = 0
        nn = 20
        while nn<=60:
            s[pn:nn] = list(map(str,s[pn:nn]))
            nt = ' '.join(s[pn:nn])
            print(nt)
            pn += 20
            nn += 20
    elif n_s>20:
        pn = 0
        nn = 20
        while nn<=40:
            s[pn:nn] = list(map(str,s[pn:nn]))
            nt = ' '.join(s[pn:nn])
            print(nt)
            pn += 20
            nn += 20
    elif n_s<20:
        s[pn:nn] = list(map(str,s[pn:nn]))
        nt = ' '.join(s[pn:nn])
        print(nt)
        
n_s = int(input())
s = []

s.extend(map(int,input().split()))
s.insert(0,5)
print(s)



h_n = int(input())
for i in range(h_n):
    g,s_n = map(int,input().split())
    temp = s_n
    if(g==1):
        num = 1
        while(s_n<=n_s):
            num += 1
            change(s,s_n)
            s_n = temp*num
    else:
        change(s,s_n)
        num=1
        while(s_n-num>=1 and s_n+num<=n_s):
            if(s[s_n-num]==s[s_n+num]):
                change(s,s_n-num)
                change(s,s_n+num)
                num += 1
            else: break

del s[0]


result(s,n_s)


    
          

                
            
            