# p11 : get the result from given list by multiplication of other elements, exclude own value.

# to_right swap, followed by, to_left swap

def product_exception_self(nums: list[int]) -> list[int]:

    output = []
    tmp = 1

    for i in range(len(nums)):
        output.append(tmp)
        tmp *= nums[i]

    tmp = 1

    for i in range(len(nums)-1, -1, -1):
        output[i] *= tmp
        tmp *= nums[i]

    return output

print(product_exception_self([1,2,3,4]))

