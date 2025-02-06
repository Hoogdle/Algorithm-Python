

# using 'in' function for checking whether target element in the given list
# 'in' function => 'target data' in 'list'
# list.index() => get the target element's index in that list

def twoSum(nums: list[int], target: int) -> list[int]:
    for i,n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            return [i, nums[i+1:].index(complement) + (i+1)]