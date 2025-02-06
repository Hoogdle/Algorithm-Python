# p10: Find biggest result by use min(a,b) to all given element.

# sort-and-pairing

def arrayPairSum(nums:list[int]) -> int:

    sum = 0
    pair = []

    nums.sort(reverse=True)

    for n in nums:
        pair.append(n)

        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum
