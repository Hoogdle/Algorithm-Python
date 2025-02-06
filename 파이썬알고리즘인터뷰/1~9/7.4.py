

# optimal solution of 7.3

def twoSum(nums:list[int], target:int)-> list[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        if target-num in nums_map:
            return [i, nums[target-num]]
        nums_map[num] = i