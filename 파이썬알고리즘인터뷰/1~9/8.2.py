

# using stack
# down-up differentiation mechanism
# pool made when there is 'inflection point'(down, down, down, (pool made) ,up)

def trap(height: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[stack[-1]] < height[i]:
            top = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            height = min(height[stack[-1]], height[i]) - height[top]

            volume += distance * height

        stack.append(i)

    return volume