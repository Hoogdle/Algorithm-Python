

# using '2-pointer'
# but we have to consider 'index', it not solvable by 2-pointer

def twoSum(nums: list[int], target: int)-> list[int]:
    left,right = 0, len(nums)-1
    nums.sort() # destroy index data

    while left<right:
        compare_num = nums[left] + nums[right]

        if compare_num < target:
            right -= 1
        elif compare_num > target:
            left += 1
        else:
            return [left,right]
