

# using dictionary(reverse)
# target - num

def twoSum(nums: list[int], target: int)-> list[int]:

    nums_map = {}

    for i,num in enumerate(nums):
        nums_map[num] = i

    for i,num in enumerate(nums):
        if target - num == nums_map and i != nums_map[target-num]:
            return[i, nums_map[target-num]]

