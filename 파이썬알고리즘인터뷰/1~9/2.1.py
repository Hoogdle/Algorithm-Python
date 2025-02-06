#p2 : make function that reverse given list. reversing operation must be occurred in given list

# using 'two-pointer'

def reverseString(s:list[str])->None:
    left,right = 0,len(s)-1

    while left<right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
