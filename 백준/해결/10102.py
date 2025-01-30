num = int(input())
vote = input()

A = 0
B = 0

for item in vote:
    if item=='A':
        A = A+1
    else:
        B = B+1

if(A>B):
    print('A')
elif(B>A):
    print('B')
else:
    print('Tie')