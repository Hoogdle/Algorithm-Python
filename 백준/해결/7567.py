plate = input()

num = len(plate)
sum = 10
for i in range(num):
    if i==(num-1):
        break
    if plate[i]==plate[i+1]:
        sum = sum + 5
    else:
        sum = sum + 10

print(sum)
