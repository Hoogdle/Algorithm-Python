

# select even number

def arrayPairSum(nums: list[int]) -> int:
    result = 0

    for i in range(0,len(nums),2):
        result += nums[i]

    return result