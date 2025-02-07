

# art of python
# ! function name should be a 'lower case' !
# slicing have useful time complexity in python!

def array_pair_sum(nums: list[int]) -> int:
    return sum(nums.sort(reverse=True)[::2])