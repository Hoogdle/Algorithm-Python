# p9: print '3-element' that result of summation is 0.

# using '3-pointer' (brute force)
# O(n^3)

def threeSum(nums: list[int]) -> list[list[int]]:
    result = []

    # for passing
    nums.sort()

    for i in range(len(nums)-2):
        if i>0 and nums[i-1] == nums[i]:
            continue
        for j in range(i+1,len(nums)-1):
            if j>i+1 and nums[j-1] == nums[j]:
                continue
            for k in range(j+1,len(nums)):
                if k>j+1 and nums[k-1] == nums[k]:
                    continue

                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result