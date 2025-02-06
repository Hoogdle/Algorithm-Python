

# using '2-pointer' O(n^2)

def threeSum(nums:list[int], target:int) -> list[list[int]]:
    result = []

    nums.sort()

    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1

        while left<right:
            comp_result = nums[i] + nums[left] + nums[right]

            if comp_result < target:
                left += 1
            elif comp_result > target:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left<right and nums[left] == nums[left+1]:
                    left += 1
                while left>right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1

    return result

