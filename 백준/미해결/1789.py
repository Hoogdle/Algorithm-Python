# 서로 다른 자연수의 Sum
# Sum given

# Q. 가장 많이 조합할 수 있는 자연수의 case에서
# case가 가지는 자연수의 수?

# not in 사용 가능!


num = int(input())
counter =[]
i=1

while True:

    if num-i >= 0 and (num-i) not in counter:
        counter.append(i)
        num = num-i
    if num-i< 0:
        break
    i = i+1

print(len(counter))


    
    


