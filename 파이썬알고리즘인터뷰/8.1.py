# p8 : Trapping Rain Water

# using '2-pointer'
# centering mechanism

def trap(height: list[int])->int:
    left, right = 0, len(list)-1
    left_max, right_max = height[left], height[right]

    volume = 0

    while left<right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume