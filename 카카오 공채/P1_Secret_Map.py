# 카카오 공채 '비밀지도'

# list comprehension order
# bit 'OR' operation
# using deque for computational efficiency

from collections import deque


def makeSecretMap(n:int, arr1:list[int], arr2:list[int])->list[list[str]]:

    results = []

    for i in range(n):
        data = bin(arr1[i] | arr2[i])
        data = deque(data[2:]) # remove '0b' token
        if len(data)<n:
            for j in range(n-len(data)):
                data.appendleft('0')

        results.append([' ' if x=='0' else '#' for x in data])

    return results


input1 = [46,33,33,22,31,50]
input2 = [27,56,19,14,14,10]
n = 6

print(makeSecretMap(n,input1,input2))
